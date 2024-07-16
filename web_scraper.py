import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a"):
        print(link.get("href"))

def main():
    url = input("Enter the URL to scrape -> ")
    scrape_website(url)

if __name__ == "__main__":
    main()

