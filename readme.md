# Amazon Product Scraper (Python + Selenium)

## 📌 Project Overview

This project is a **Python-based web scraping automation tool** that extracts detailed product information from **Amazon India** based on a user’s search query. The scraper automatically navigates through search result pages, opens individual product pages, collects structured product data, and exports the results into an **Excel file** for further analysis.

This project is built mainly for **learning, practice purposes**.

---

## 🎯 Objectives

* Automate product search on Amazon
* Handle **dynamic content** using Selenium
* Extract detailed product-level information
* Store data in a clean, structured format
* Export final data to **Excel (.xlsx)** using Pandas

---

## 🛠️ Technologies & Libraries Used

* **Python 3** – Core programming language
* **Selenium** – Browser automation & dynamic content handling
* **Chrome WebDriver** – Automates Google Chrome
* **Pandas** – Data storage and Excel export
* **BeautifulSoup (bs4)** – HTML parsing (optional / future use)
* **OS & Time modules** – File handling and delays

---

## ⚙️ Features

* Headless browser execution (runs without UI)
* Automated scrolling to load lazy-loaded content
* Multi-page navigation (Next page handling)
* Safe element extraction with error handling
* Extracts both **text data** and **tabular specifications**
* Stores output in Excel format
* Configurable product search via user input

---

## 📂 Data Extracted

For each product, the scraper collects:

* Product Title
* Price & Actual Price
* Discount / Savings Percentage
* Review Count
* Star Ratings
* Store / Brand Name
* Offers & Promotional Messages
* Product Variants
* Bullet-point Descriptions
* Technical Specifications (tables)

---

## 🔄 Workflow Explanation

1. User enters a **search keyword** (e.g., mobile phones)
2. Script opens Amazon India in headless Chrome
3. Product search is performed automatically
4. All product URLs are collected from result pages
5. Each product page is opened individually
6. Product data is safely extracted
7. Data is stored in a list of dictionaries
8. Pandas converts data into a DataFrame
9. Final output is saved as an Excel file

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites

* Python installed (3.8+ recommended)
* Google Chrome installed
* ChromeDriver matching your Chrome version

### 2️⃣ Install Required Libraries

```bash
pip install selenium pandas bs4 openpyxl
```

### 3️⃣ Update ChromeDriver Path

Update the following line in the script:

```python
path = "D:/Web Scraping/chromedriver-win64/chromedriver.exe"
```

### 4️⃣ Run the Script

```bash
python scraper.py
```

### 5️⃣ Output

An Excel file will be generated:

```
<search_text>_data.xlsx
```

---

## 🧪 Error Handling & Stability

* Uses `try-except` blocks to avoid crashes
* Handles missing elements gracefully
* Uses delays (`time.sleep`) to prevent page load issues
* Stops scraping after a defined limit (100 products)

---

## ⚠️ Important Notes

* This project is intended for **educational purposes only**
* Web scraping should always respect **website terms & policies**
* Avoid excessive requests to prevent IP blocking




