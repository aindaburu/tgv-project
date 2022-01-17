import requests

URL = 'https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&facet=date&facet=origine&facet=destination&facet=od_happy_card'

def request_tgvmax():
    r = requests.get(URL)
    print(r.json())

