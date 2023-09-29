# Zillow Web Scraper and Google Sheets Uploader

This Python project is designed to scrape rental property listings from Zillow and upload the gathered data to a Google Sheets form. It utilizes web scraping techniques, Selenium for browser automation, and the Google Forms API to achieve this task.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before running this project, you need to ensure you have the following prerequisites installed:

- **Python**: This project is written in Python, so you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

- **Google Chrome**: The project uses Selenium with Chrome WebDriver. Make sure you have Google Chrome installed on your machine.

- **Chrome WebDriver**: Download and install the Chrome WebDriver for Selenium. You can find it [here](https://sites.google.com/chromium.org/driver/).

- **Required Python Packages**: Install the required Python packages using pip:

  ```bash
  pip install requests beautifulsoup4 selenium
  ```

- **Google Account**: You'll need a Google account to create and use the Google Sheets form. Make sure to create one if you don't have it.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ozesince02/Property-Listing-Data-Collection-and-Google-Sheets-Integration.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name
   ```

3. Update the Chrome WebDriver path in the `chrome_driver_path` variable in the script with the correct path to your WebDriver executable.

## Usage

To use this project, follow these steps:

1. Run the script:

   ```bash
   python zillow_scraper.py
   ```

2. The script will scrape rental property listings from Zillow and open a Google Sheets form in a Chrome browser window.

3. It will input the scraped data into the form one by one.

4. After processing all listings, the script will close the browser window.

## Configuration

Before running the script, make sure to configure the following variables in the `zillow_scraper.py` script:

- `GOOGLE_SHEET_URL`: The URL of the Google Sheets form where you want to upload the data.

- `ZILLOW_LINK`: The URL of the Zillow search results page you want to scrape.

- `chrome_driver_path`: The path to the Chrome WebDriver executable on your system.

## Contributing

Contributions to this project are welcome. You can contribute by submitting bug reports, feature requests, or by making direct code contributions through pull requests.

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your commit message here"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request on the original repository with a clear description of your changes.

## Credits

This project was completed as part of a learning experience, with instruction provided by Angela Yu.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
