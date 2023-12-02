'''
This file contains the GoogleSearch class that is responsible for performing a search on Google.
'''
import requests
from bs4 import BeautifulSoup
class GoogleSearch:
    def search(self, keywords):
        search_result = []
        # Perform a search on Google
        query = ' '.join(keywords)
        url = f"https://www.google.com/search?q={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Retrieve the top search result
        top_result = soup.find('div', class_='BNeawe vvjwJb AP7Wnd')
        if top_result:
            search_result.append(top_result.text)
        return search_result