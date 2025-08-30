

from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import time 
from bs4 import BeautifulSoup as BS
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
 
from selenium.webdriver.common.by import By

import csv
import os
import pandas as pd
path ="D:/Web Scraping/chromedriver-win64/chromedriver.exe"
s = Service(path)
driver = webdriver.Chrome(service = s)
driver.get("https://www.amazon.in/s?k=samsang+phone&rh=n%3A1389401031&ref=nb_sb_noss")
time.sleep(4)
height = driver.execute_script("return document.body.scrollHeight")

#print(height)
while True:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # when there is window.scrollTo it will return NONE
    time.sleep(4)
    
    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break
    height=new_height





products=driver.find_elements("css selector",".a-link-normal.s-line-clamp-2.s-line-clamp-3-for-col-12.s-link-style.a-text-normal")
url = []
for u in products:
    url.append(u.get_attribute("href"))
driver.quit()



data=[]
def run_scraper(url):
    
    path ="D:/Web Scraping/chromedriver-win64/chromedriver.exe"
    s = Service(path)
    driver = webdriver.Chrome(service = s)
    driver.get(url)
    time.sleep(4)
    height = driver.execute_script("return document.body.scrollHeight")
    wait = WebDriverWait(driver, 10)
    #print(height)
    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # when there is window.scrollTo it will return NONE
        time.sleep(4)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if height == new_height:
            break
        height=new_height
    
    
    
    def safe_find_text(driver, selector, by=By.CSS_SELECTOR):
        """Try to find element text; return empty string if not found."""
        try:
            return driver.find_element(by, selector).text.strip()
        except:
            return ""  # or None if you prefer
  
    
    tittle = safe_find_text(driver, "#productTitle")
    reviwCount = safe_find_text(driver, "#acrCustomerReviewText")
    price = safe_find_text(driver, ".priceToPay")
    margin = safe_find_text(driver, ".savingsPercentage")
    ActualPrice = safe_find_text(driver, ".a-price.a-text-price")
    Store = safe_find_text(driver, "#bylineInfo")
    stars = safe_find_text(driver, ".reviewCountTextLinkedHistogram.noUnderline")
    socialProofing = safe_find_text(driver, ".social-proofing-faceout-title")
    msg = safe_find_text(driver, "#vatMessage_feature_div")
    offers = safe_find_text(driver, ".a-carousel-viewport")
    allVarinet = safe_find_text(driver, "#inline-twister-expander-content-size_name")
    
    # Alldescription list
    Alldescription = []
    try:
        Description = driver.find_elements(By.CSS_SELECTOR, "#feature-bullets span.a-list-item")
        for d in Description:
            Alldescription.append(d.text.strip())
    except:
        Alldescription = []
    
    # data_dict2 from table
    data_dict2 = {}
    try:
        table = driver.find_element(By.CSS_SELECTOR, ".a-spacing-top-small table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 2:
                key = cols[0].text.strip()
                value = cols[1].text.strip()
                data_dict2[key] = value
    except:
        data_dict2 = {}
    
    # data_dict from product details table
    data_dict = {}
    try:
        tables = driver.find_elements(By.CSS_SELECTOR, "#productDetails_feature_div .prodDetTable")
        for t in tables:
            rows = t.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                try:
                    key = row.find_element(By.TAG_NAME, "th").text.strip()
                except:
                    key = ""
                try:
                    value = row.find_element(By.TAG_NAME, "td").text.strip()
                except:
                    value = ""
                if key:
                    data_dict[key] = value
    except:
        data_dict = {}
    
    # Combine fields
    fileds = ['tittle','reviwCount','price','margin','ActualPrice','Store','stars',
              'socialProofing','msg','offers','allVarinet']
    fileds.extend(list(data_dict2.keys()))
    fileds.append("Alldescription")
    fileds.extend(list(data_dict.keys()))
    
    print(fileds)
  
   
    # Check if file exists
    file_exists = os.path.isfile("PhoneDetails.csv")
    
    # Merge all data into a single row dictionary
    row = {
        'tittle': tittle,
        'reviwCount': reviwCount,
        'price': price,
        'margin': margin,
        'ActualPrice': ActualPrice,
        'Store': Store,
        'stars': stars,
        'socialProofing': socialProofing,
        'msg': msg,
        'offers': offers,
        'allVarinet': allVarinet,
        'Alldescription': Alldescription
    }
    
    # Merge data_dict and data_dict2 into the row
    row.update(data_dict)
    row.update(data_dict2)
    
    # Write to CSV
    # with open('PhoneDetails.csv', 'a', encoding='utf-8', newline='') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fileds)
        
    #     # Write header only if file is new
    #     if not file_exists:
    #         writer.writeheader()
        
    #     # Write the row
    #     writer.writerow(row)
    
    print("Data appended successfully ✅")
    
    driver.quit()
    return row
count = 0
data =[]

for u in url:
    
    
    
    row =run_scraper(u)
    data.append(row)
    print(u)
    time.sleep(2)
    # driver.back()
    #print(driver.current_url)
    count+=1
print(count)
df = pd.DataFrame(data)
df 
    

df.to_csv('dataphone.csv') 
