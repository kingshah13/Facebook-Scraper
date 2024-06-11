# Facebook Page Scraper
This script was tested on the page I am an admin of. If you use to scrape public pages Let me know how it goes for you.
A Python script with a GUI to scrape posts from a Facebook page using the Facebook Graph API. This tool allows you to filter posts by creation date and save the data to an Excel file.

## Features
- GUI for easy input of Access Token, Page ID, date range, and fields to scrape.
- Fetch posts from a specified Facebook page within a date range.
- Save the scraped data to an Excel file.

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
     git clone https://github.com/your-username/Facebook-Scraper.git
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
   - **Access Token**: Enter your Facebook Graph API access token.
   - **Page ID**: Enter the ID of the Facebook page you want to scrape.
   - **Since (YYYY-MM-DD)**: Enter the start date for the posts you want to scrape.
   - **Until (YYYY-MM-DD)**: Enter the end date for the posts you want to scrape.
   - **Fields to Scrape**: Select the fields you want to include in the scraped data.
   - Click the "Run Scraper" button.

3. **Output**:
   - The data will be saved to an Excel file named `facebook_posts.xlsx` in the same directory.

## Notes
- Ensure your access token is kept secure and not shared publicly.
- The date format should be `YYYY-MM-DD`.

## Troubleshooting
- If you encounter any issues, ensure you have the correct permissions for the access token.
- Check the date format and ensure it's valid.
- Make sure all required fields are filled in the GUI before running the scraper.

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.
