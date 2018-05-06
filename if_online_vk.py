import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text

def main():
    url = 'https://vk.com/durov'
    link = get_html(url)
    soup = BeautifulSoup(link, 'lxml')
    print(soup.find('title').text, end = ': ')
    print(soup.find('span', class_='pp_last_activity_text').text)


if __name__ == '__main__':
    main()
