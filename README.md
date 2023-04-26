# YC Company Scraper

YC Company Scraper is a Python script that fetches information about Y Combinator companies from specified batches, extracts GitHub repository links from their websites, and prints the data.

## Features

- Retrieve company information from various Y Combinator batches
- Scrape GitHub repository links from company websites
- Print the extracted data

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository:
```
git clone 
cd yc-company-scraper

```markdown

2. Install the `requests` library:
```



pip install requests

```markdown

## Usage

1. Open `yc_company_scraper.py` and modify the `batches` list to include the desired Y Combinator batch codes.

2. Run the script:
```



python yc_company_scraper.py

```python

3. The script will print the company name, website, YC URL, and any GitHub repository links found on their website.

## Disclaimer

This script is for educational purposes only. Always respect the websites' terms of service and robots.txt when scraping data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.