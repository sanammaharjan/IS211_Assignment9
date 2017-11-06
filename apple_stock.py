import urllib2
from bs4 import BeautifulSoup as BS
import json

link = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
data = urllib2.urlopen(link)
soup = BS(data.read(), "html.parser")

def stock():
    data = []
    fhandler = soup.find_all('tr')

    for tdata in fhandler:
        try:
            if len(tdata.find_all(('td', {'class': 'yfnc_tabledata1'}))) == 7:
                date = tdata.contents[0].get_text()
                close_price = tdata.contents[6].get_text()
                data.append((date, close_price))

                #defining json string
                json_string = {
                    "Date": date,
                    "Close_Price": close_price,
                }
                print(json.dumps(json_string))
        except:
            print 'Please double check the data, something went wrong'
            continue
    return stock

if __name__ == "__main__":
    stock()