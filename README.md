#Web Scraping
# 1)Amazon Product Scraper - iPhone 16 (India)
This Python project scrapes product details such as title, price, and rating from the Amazon India
search results page for "iPhone 16". It uses `requests`, `BeautifulSoup`, and `pandas` to extract and
save data to a CSV file.
## Features
- Scrapes Amazon India for "iPhone 16" listings.
- Extracts product title, price, and rating.
- Stores data in a CSV format.
- Mimics browser headers to avoid bot detection.
- Includes random delay to reduce the risk of blocking.
## Output
The extracted data will be saved to:
```
amazon_iphone.csv
```
## Requirements
Install the following Python packages before running the script:
```bash
pip install requests beautifulsoup4 pandas
```
## Disclaimer

This project is intended **solely for educational and personal learning purposes**.

Web scraping Amazon.com or Amazon.in **violates their Terms of Service**.  
This code is not intended for production use, commercial use, or large-scale data extraction.
Use responsibly and respect the website's terms and infrastructure.
