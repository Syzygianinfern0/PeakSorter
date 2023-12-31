# PeakSorter
REI Review Analytics

## Overview

PeakSorter is a Python script designed to enhance the product comparison experience on REI's website. 
It scrapes product data and generates a sorted table based on the popularity of items, as indicated by the number of reviews. 
This tool is invaluable for outdoor enthusiasts and shoppers looking to make informed decisions based on community feedback.

## Features

- **Data Scraping**: Extracts product details such as brand, name, price, sale price, number of reviews, and ratings from REI's product pages.
- **Sorting Mechanism**: Organizes products by the number of reviews, highlighting the most popular items.
- **User-friendly Display**: Presents data in a clear, concise table format, both in the console and as CSV output.

## How It Works

The script uses Python's `requests` and `BeautifulSoup` libraries to scrape product data from REI's website. It then utilizes the `rich` library to display the data in a well-formatted table, making it easy to read and compare products.

## Usage

1.  Clone the repository.
2.  Install the required libraries using `pip install -r requirements.txt`.
3.  Run the script with `python peaksorter.py`.
4.  View the generated table in the console, or find the CSV output for the top 10 products.

## Notes

PeakSorter is designed for educational and personal use. Please be aware of REI's terms of service regarding web scraping.
This script is not affiliated with, endorsed by, or in any way officially connected with REI. It was developed as a tool for personal use and learning purposes.

You can adjust the content as needed to fit your project's specifics and personal style. This README provides a basic structure and covers key aspects such as an overview, features, usage instructions, and disclaimers.

---

This README was created with ❤️ by GPT4.
