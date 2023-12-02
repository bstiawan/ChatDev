'''
This is the main file that contains the entry point of the application.
'''
from tkinter import Tk, Label, Entry, Button
from website_analyzer import WebsiteAnalyzer, WebsiteInfo
from google_search import GoogleSearch
class App:
    def __init__(self, master):
        self.master = master
        master.title("Website Analyzer")
        self.label = Label(master, text="Enter URL:")
        self.label.pack()
        self.entry = Entry(master)
        self.entry.pack()
        self.analyze_button = Button(master, text="Analyze", command=self.analyze_website)
        self.analyze_button.pack()
    def analyze_website(self):
        url = self.entry.get()
        # Analyze the website
        analyzer = WebsiteAnalyzer()
        website_info = analyzer.analyze(url)
        # Search on Google
        search = GoogleSearch()
        search_result = search.search(website_info.keywords)
        # Generate article list
        articles = self.generate_articles(search_result)
        # Display the articles
        self.display_articles(articles)
    def generate_articles(self, search_result):
        articles = []
        for result in search_result:
            articles.append(f"Article: {result}")
        return articles
    def display_articles(self, articles):
        for article in articles:
            print(article)
root = Tk()
app = App(root)
root.mainloop()