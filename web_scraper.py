import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")

soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a["title"]
    
     rating = book.select_one("p[class^='star-rating']")["class"][1]
    
    price = book.select_one("p[class='price_color']").get_text(strip=True)

    print(f"Book titled: {title} has a rating of: {rating} stars and a price of: {price}")
