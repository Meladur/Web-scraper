import requests
from bs4 import BeautifulSoup

def get_book_info(book):
    title = book.h3.a["title"]
    rating = book.select_one("p[class^='star-rating']")["class"][1]
    price = book.select_one("p[class='price_color']").get_text(strip=True)
    return f"Book titled: {title} has a rating of: {rating} stars and a price of: {price}"

def scrape_books(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for errors in the HTTP response
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find_all("article")

def main():
    url = "https://books.toscrape.com/"
    books = scrape_books(url)

    for book in books:
        print(get_book_info(book))

if __name__ == "__main__":
    main()
