import requests
from bs4 import BeautifulSoup

# Список ключевых слов для поиска
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = "https://habr.com/ru/articles/"
response = requests.get(URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('article')

for i in articles:
    title_article = i.find('h2')
    if title_article:
        title = title_article.text.strip()
        href = title_article.find('a')['href']
        link = f"https://habr.com{href}"
    else:
        continue

    article_response = requests.get(link)
    article_response.raise_for_status()
    article_soup = BeautifulSoup(article_response.text, 'html.parser')
    article_text = article_soup.get_text().lower()

    if len([keyword.lower() in article_text for keyword in KEYWORDS]) != 0:
        date_article = i.find('time')
        if date_article:
            date = date_article['title']
        else:
            date = "Дата не найдена"
        print(f"{date} – {title} – {link}")
