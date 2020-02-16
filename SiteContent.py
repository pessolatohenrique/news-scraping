import requests
from bs4 import BeautifulSoup

class SiteContent:
    def __init__(self, subject, name,url, container, title, tag_title, published):
        self._subject = subject
        self._name = name
        self._url = url
        self._container = container
        self._title = title
        self._tag_title = tag_title
        self._published = published

    def show_info(self, figure, title, published_at):
        print(f"- {title.strip()}, publicada em {published_at.strip()}. \n Imagem referência: {figure}\n")

    def get_url_search(self):
        return f'{self._url}?q={self._subject._name}'

    def get_figure_url(self, news):
        figure = news.find('img')
        figure_url = '#N/D'

        if (figure is not None):
            figure_url = news.find('img').get('src')

            if (figure_url == None):
                figure_url = news.find('img').get('data-src')

        return figure_url

    def get_title(self, news):
        title = news.find(class_=self._title)

        if (self._tag_title):
            title = title.find(self._tag_title)

        title = title.contents[0]

        return title

    def search(self):
        url = self.get_url_search()
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        container_list = soup.find_all(class_=self._container)

        print(f"\n***{self._name}***\n")

        for news in container_list:
            figure_url = self.get_figure_url(news)
            title = self.get_title(news)
            published_at = news.find(class_=self._published).contents[0]
            self.show_info(figure_url, title, published_at)
