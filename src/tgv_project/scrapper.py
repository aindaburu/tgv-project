"""
This code aims at scrapping real-time data from tgvmax.com.
"""

import requests

API_URL = 'https://data.sncf.com/api/records/1.0'


def generate_search_url(date, origine, destination):
    """
    Scrapping data from API_URL.
    """
    url = f"{API_URL}/search/?dataset=tgvmax&q=&facet=date&facet=origine&facet=destination&" \
          f"refine.origine={origine}&refine.date={date}&refine.destination={destination}"
    new_url = url.replace(" ", "+")
    return new_url


def scrap_trip(date, origine, destination):
    """
    Making the HTTP request.
    """
    search_url = generate_search_url(date, origine, destination)
    response = requests.get(search_url)
    return response.json()
