'''
This file contains the WebsiteAnalyzer class that is responsible for analyzing the content of a website.
'''
import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlparse
class WebsiteAnalyzer:
    def analyze(self, url):
        website_info = WebsiteInfo()
        # Analyze the content of the website
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract relevant information
        website_info.title = soup.title.string.strip() if soup.title else ""
        website_info.keywords = self.extract_keywords(soup)
        website_info.links = self.extract_links(url, soup)
        return website_info
    def extract_keywords(self, soup):
        # Extract keywords from the website content
        text = soup.get_text()
        words = text.split()
        # Remove common words and punctuation
        common_words = ['the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'hot', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she', 'which', 'do', 'their', 'time', 'if', 'will', 'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over', 'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side', 'been', 'now', 'find', 'any', 'new', 'work', 'part', 'take', 'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me', 'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form', 'sentence', 'great', 'think', 'say', 'help', 'low', 'line', 'differ', 'turn', 'cause', 'much', 'mean', 'before', 'move', 'right', 'boy', 'old', 'too', 'same', 'tell', 'does', 'set', 'three', 'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', 'don\'t', 'while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose', 'leave', 'song', 'measure', 'door']
        punctuation = ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '~']
        # Count the frequency of each word
        word_count = Counter(words)
        # Remove common words and punctuation
        keywords = [word for word in word_count.keys() if word.lower() not in common_words and word not in punctuation]
        return keywords
    def extract_links(self, url, soup):
        # Extract all links from the website
        links = []
        parsed_url = urlparse(url)
        base_url = parsed_url.scheme + "://" + parsed_url.netloc
        for link in soup.find_all('a'):
            href = link.get('href')
            # Ignore empty and non-http links
            if href and href.startswith('http'):
                # Handle relative links
                if href.startswith('/'):
                    href = base_url + href
                links.append(href)
        return links
class WebsiteInfo:
    def __init__(self):
        self.title = ""
        self.keywords = []
        self.links = []