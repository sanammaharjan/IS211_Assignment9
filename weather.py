import urllib2
from bs4 import BeautifulSoup as BS
link = urllib2.Request("https://www.wunderground.com/history/airport/"
                       "KNYC/2015/1/1/MonthlyCalendar.html")
data = urllib2.urlopen(link)
soup = BS(data.read(), 'html.parser')
table_data = soup.find_all('td')

def weather():
    for row in table_data:
        if "class" in row.attrs and "day" in row['class']:
            daily_temp = row.find_all('td')
            for row1 in daily_temp:
                if "class" in row1.attrs and "date-link" in row1['class']:
                    a_table = row1.find_all('a')
                    for row10 in a_table:
                        if "class" in row10.attrs and "dateText" in \
                                row10['class']:
                            date = int(row10.string)
                            print "Day of the Month: %i" % date
            data_available = False
            for row2 in daily_temp:
                if "class" in row2.attrs and "value-header" in \
                        row2['class'] and (row2.string == "Actual:"\
                                             or row2.string == "Forecast:"):
                    daily_temp_temp = row2.parent
                    type_of_temp = daily_temp_temp.find("td").string[:-1]
                    temperature_list = daily_temp_temp.find_all("span")
                    for row20 in temperature_list:
                        if "class" in row20.attrs and "high" in \
                                row20['class']:
                            print "  %s High: %s" % (type_of_temp,
                                                     row20.string)
                            data_available = True
                        if "class" in row20.attrs and "low" in \
                           row20['class']:
                            print "  %s Low: %s" % (type_of_temp,
                                                    row20.string)
                            data_available = True
            if data_available is False:
                print "  Data not Available"

if __name__ == "__main__":
    weather()