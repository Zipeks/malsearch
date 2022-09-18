from urllib import response
from webbrowser import get
import requests
import json
import time
import re
def get_titles(a):
    f = open("titles2.txt", "a")
    for n in range(550,a+1):
        print(n)
        respone =  requests.get(f'https://api.jikan.moe/v4/top/anime?page={n}&filter=bypopularity')

        parsed = json.loads(respone.content)

        for each in range(0,len(parsed["data"])):
            title = parsed['data'][each]['title_english']
            if title == None:
                title = parsed['data'][each]['title']
            # print(title)
            f.write(f"{title}\n")
        time.sleep(1.01)

    f.close()
# get_titles(700)

def search():
    with open('titles.txt', 'r') as titles:
        for line in titles:
            line = line.rstrip()
            table = line.split(" ")
            if re.search("^[sca]", table[0], re.I):
               if len(table)>1 and re.search("^[sca]", table[1], re.I) and len(table):
                    if len(table)>2 and re.search("^[sca]", table[2], re.I) and len(table)<4:
                        print(line)
search()