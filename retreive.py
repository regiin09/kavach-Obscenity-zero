import requests
from bs4 import BeautifulSoup

def get_text_content(url):
    # Send a request to the website and retrieve the HTML code
    response = requests.get(url)
    html = response.content

    # Parse the HTML code with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all text content on the website and store it in a list
    text_content = []
    for tag in soup.find_all(text=True):
        if tag.parent.name not in ['script', 'style']:
            text_content.append(tag.string.strip())

    # Return the text content
    return text_content
