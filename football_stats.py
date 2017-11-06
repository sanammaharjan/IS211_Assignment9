import urllib2
from bs4 import BeautifulSoup as BS
import json

link = 'https://www.cbssports.com/nfl/stats/playersort/' \
       'nfl/year-2017-season-regular-category-touchdowns'
data = urllib2.urlopen(link)
soup = BS(data.read(), "html.parser")

def FStat():
    data_list = []
    fhandler = soup.find_all(class_={'row1', 'row2'})
    for tdata in fhandler[:20]:
        try:
            player_name = tdata.contents[0].get_text()
            player_position = tdata.contents[1].get_text()
            player_team = tdata.contents[2].get_text()
            touch_downs = tdata.contents[6].get_text()

            # defining json strings
            json_string = {
                "Name": player_name,
                "Position": player_position,
                'Team': player_team,
                "Touchdowns": touch_downs
            }
            print json.dumps(json_string)

        except:
            print 'Please double check the data, something went wrong'
            continue
    return data_list

if __name__ == "__main__":
    FStat()