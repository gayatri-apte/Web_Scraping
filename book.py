from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URL ="https://books.toscrape.com/"

products=[]

response = requests.get(URL, headers=HEADERS, timeout=10)

if response.status_code==200:
    soup = BeautifulSoup(response.content,"html.parser")

    result = soup.find_all("article", class_="product_pod")
    for item in result:
        #title
        title_tag = item.h3
        title = title_tag.text.strip() if title_tag else "N/A"

        #price
        price_tag = item.find("p", class_="price_color")
        price = price_tag.text.strip() if price_tag else "N/A"

        #star
       
        star_tag = item.find("p", class_="star-rating")
        if star_tag and "class" in star_tag.attrs:
           star_classes = star_tag["class"]
           star = [cls for cls in star_classes if cls != "star-rating"][0]  # e.g. 'Three'
        else:
           star = "N/A"

        products.append(
            {
                "Title":title,
                "Price":price,
                "Star":star
            }
        )

        time.sleep(random.uniform(0.5, 1.5))

else:
    print("Failed to connect to books website.",response.status_code)
df=pd.DataFrame(products)
df.to_csv("books_info.csv", index=False, encoding="utf-8")
print("Scraped",len(products),"products saved to csv file")
