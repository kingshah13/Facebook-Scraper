import requests
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

def fetch_facebook_data(access_token, page_id, fields, since, until):
    url = f"https://graph.facebook.com/v14.0/{page_id}/posts"
    params = {
        'access_token': access_token,
        'fields': ','.join(fields),
        'since': since,
        'until': until,
        'limit': 100  # Adjust this limit as needed
    }

    posts = []
    while True:
        response = requests.get(url, params=params)
        data = response.json()

        if 'data' in data:
            posts.extend(data['data'])
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
        else:
            break

    return posts

def save_to_excel(data, fields, filename="facebook_posts.xlsx"):
    df = pd.DataFrame(data, columns=fields)
    df.to_excel(filename, index=False)

def run_scraper():
    access_token = token_entry.get()
    page_id = page_id_entry.get()
    since = since_entry.get()
    until = until_entry.get()
    fields = [field for field, var in field_vars.items() if var.get()]

    if not access_token or not page_id or not since or not until:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        since_date = datetime.datetime.strptime(since, "%Y-%m-%d")
        until_date = datetime.datetime.strptime(until, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Date format should be YYYY-MM-DD")
        return

    try:
        data = fetch_facebook_data(access_token, page_id, fields, since_date.timestamp(), until_date.timestamp())
        save_to_excel(data, fields)
        messagebox.showinfo("Success", "Data has been saved to facebook_posts.xlsx")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = Tk()
root.title("Facebook Page Scraper")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Access Token").grid(column=1, row=1, sticky=W)
token_entry = ttk.Entry(mainframe, width=50)
token_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Page ID").grid(column=1, row=2, sticky=W)
page_id_entry = ttk.Entry(mainframe, width=50)
page_id_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Since (YYYY-MM-DD)").grid(column=1, row=3, sticky=W)
since_entry = ttk.Entry(mainframe, width=50)
since_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Until (YYYY-MM-DD)").grid(column=1, row=4, sticky=W)
until_entry = ttk.Entry(mainframe, width=50)
until_entry.grid(column=2, row=4, sticky=(W, E))

field_vars = {}
fields = ["id", "created_time", "message", "story", "permalink_url", "full_picture", "comments", "likes", "shares"]
ttk.Label(mainframe, text="Fields to Scrape").grid(column=1, row=5, sticky=W)

for i, field in enumerate(fields):
    var = BooleanVar()
    field_vars[field] = var
    ttk.Checkbutton(mainframe, text=field, variable=var).grid(column=2, row=5+i, sticky=W)

ttk.Button(mainframe, text="Run Scraper", command=run_scraper).grid(column=2, row=5+len(fields), sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
