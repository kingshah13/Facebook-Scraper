# Facebook Page Scraper
This script is created to scrape pages you are owner or admin of. It does not scrape public pages.

A user-friendly GUI application to scrape public Facebook pages using the Facebook Graph API. This tool allows you to configure the page, date range, and data fields to be scraped, and saves the data into an Excel file.

## Features
- Intuitive GUI: Easily input your Access Token, Page ID, date range, and select data fields with checkboxes.
- Rate Limiting: Manage the request rate to stay within Facebook's rate limits.
- Dark and Light Mode: Automatically adapts to your Windows theme.
- Data Export: Save the scraped data to an Excel file with a custom name.
- Remember Access Token: Option to securely save your access token for future use.

## Prerequisites

1. **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Facebook Graph API Access Token**: You need a valid Facebook Graph API access token with the following permissions:
   - `pages_read_engagement`
   - `pages_read_user_content`
   - `pages_show_list`
   - `pages_manage_metadata`
   - `pages_manage_engagement`

## Installation

1. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Run the following command to clone the repository:
     ```sh
     git clone https://github.com/kingshah13/Facebook-Scraper.git
     ```
   - Navigate to the cloned directory:
     ```sh
     cd facebook-page-scraper
     ```

2. **Install Dependencies**:
   - Run the following command to install the required Python libraries:
     ```sh
     pip install -r requirements.txt
     ```

## Usage

1. **Run the Script**:
   - In the terminal or command prompt, ensure you are in the `facebook-page-scraper` directory.
   - Run the script using Python:
     ```sh
     python facebook_scraper.py
     ```

2. **Fill in the GUI Fields**:
- **Access Token**: Your Facebook Graph API access token.
- **Page ID**: The ID of the Facebook page you want to scrape.
- **Since**: Start date (YYYY-MM-DD) to scrape posts from.
- **Until**: End date (YYYY-MM-DD) to scrape posts until.
- **Save As**: Filename to save the scraped data.
- **Rate Limit**: Number of requests per second (up to 1000).
- **Remember Access Token**: Checkbox to save the access token for future use.
- **Check All**: Checkbox to select all data fields.
- **Data Fields**: Select individual fields to scrape.

## Notes
- Ensure your access token is kept secure and not shared publicly.
- The date format should be `YYYY-MM-DD`.

## Troubleshooting
- If you encounter any issues, ensure you have the correct permissions for the access token.
- Check the date format and ensure it's valid.
- Make sure all required fields are filled in the GUI before running the scraper.

## License
This project is licensed under the MIT License.
