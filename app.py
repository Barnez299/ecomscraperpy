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
        sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0]
    except:
        sold = ''

    # print(sold)


def main():
    url = 'https://www.ebay.com/itm/Mens-Sport-Watches-LED-Date-Waterproof-Digital-Quartz-Military-Wrist-Watch/143669951342?_trkparms=ispr%3D1&hash=item2173657b6e:g:3wAAAOSwvBBZ4X2U&enc=AQAFAAACYBaobrjLl8XobRIiIML1V4Imu%2Fn%2BzU5L90Z278x5ickk7d4nremBkvNKtcC0ZwqXDMlKw2CYo88KT4XRlQBrzRMfLUtiX5irh%2FPpa7tta3CTXQ3zmhIU85g2iGVXRygj3Oh87Ahnu3rjxH%2F9A2jh7Mc65Dy4hJZWuZT2%2Fb4xCyXs1azTE9vD0wKmjz9eqyuC22SUJ064JejjeanyZoIs%2FayR6g81PFdDZmgbkcTN8C1GYgDTjopU10mO%2FVgZIcjDMzkjZfiS%2Fl2suwH1JrxcaYwDcjlxEr5wdQSl7VPkRr3m4%2FQyiKpx0qTlNc1X2L%2BLT4qDAlPlRSlw29oqFFNIMn249vaB9A3B6ZlpPSGWRkaFwaBvvHQrjLstjryBSUjqw5ybGZrTuhyIBXRl3iR6H6kKL%2FQXTh9v7S%2FKcW4qLhSdgAUhoAfrSve%2FDBmap39vghe8GAYRyygHG7yqxigoIRvbWOt0igVAaXb7JDgBIsTxvGyb3E86f9NXQnRnTrkfj69Qe3vWmqxnu8Qno4ggCXiWFERI0CTOjSEMB5rgyryEy%2FgYg870pI9PGLPLYx3035l8YTW9JnF8ZA8D8ANkYjppMzG1hcir2z4IJCV2ETr89F84mbLs9fkcB%2BPFd6SGmBSTmo1hKb30Ii%2BqrIWh24Sp1hEBw7FugA7neJ7A30dfHO8N0Mp7asyysPDvwQFUUsoEijBaJxyNJSc2HusI9VslHwPn0zR0SN3nlJSKdSfUli7E6i6uFyOFFOEPu1wCHRZBA3%2BBZcuEP3LrQ8wkD94CccGpBouHpNI8foYCwJSo&checksum=14366995134259a4ad4a37c9480b91923c15b2a1d6d7'

    

    
    get_detail_data(get_page(url))
















if __name__ == '__main__':
    main()