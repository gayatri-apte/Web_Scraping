from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URL = "https://www.amazon.in/s?k=iphone+16&crid=3T4K72PNKLLAT&sprefix=%2Caps%2C179&ref=nb_sb_ss_recent_1_0_recent"

products = []
response = requests.get(URL, headers=HEADERS, timeout=10)

if response.status_code==200:
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", {"data-component-type": "s-search-result"})

    for item in results:
        #title
        title_tag = item.h2
        title = title_tag.text.strip() if title_tag else "N/A"
        
        #price
        price_tag = item.find("span",class_="a-price-whole")
        price = price_tag.text.strip() if price_tag else "N/A"
        
        #Rating
        rating_tag = item.find("span", class_="a-icon-alt")
        rating = rating_tag.text.strip() if rating_tag else "N/A"

        products.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

        time.sleep(random.uniform(0.5, 1.5))

else:
    print("Failed to connect to Amazon",response.status_code)

df = pd.DataFrame(products)
df.to_csv("amazon_iphone.csv",index=False, encoding="utf-8")
print("Scarped", len(products),"products saved to csv file")


