import csv

import requests
from bs4 import BeautifulSoup




def get_page(url):
    response = requests.get(url)
    
    if not response.ok:
        print('server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')

    return soup

def get_detail_data(soup):
# headline title
# price
# items sold

    try:    
        # title = soup.find('h1', id="itemTitle").text.strip().split()[-1]
        title = soup.find('h1', {'class': 'it-ttl'}).contents[-1].strip()
    except:
        title = ''
    # print(title)

    try:
        pr = soup.find('span', id='prcIsum').text.strip()
        currency, price = pr.split(' ')
    except:
        price = ''
        currency = ''

    # print(price)
    # print(currency)

    try:
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0].replace('\xa0', '')
    except:
        sold = ''

    # print(sold)


    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total sold': sold
    }

    return data

def get_index_data(soup):

    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    # hrefs only

    urls = [item.get('href') for item in links]

    return urls







def main():
    url = 'https://www.ebay.com/sch/i.html?_nkw=mens+watches&_pgn=1'

    

    
    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        print(data)
















if __name__ == '__main__':
    main()