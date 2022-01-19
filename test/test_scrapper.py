"""
Test all the functions.
"""

from tgv_project.scrapper import scrap_trip, generate_search_url


def test_generate_search_url():
    """
    Test of url search.
    """
    url = generate_search_url("2022-01-31", "BAYONNE", "PARIS (intramuros)")
    assert url == "https://data.sncf.com/api/records/1.0/search/?dataset=tgvmax&q=&facet=date&" \
                  "facet=origine&facet=destination&refine.origine=BAYONNE&refine.date=2022-01-31&" \
                  "refine.destination=PARIS+(intramuros)"


def test_scrap_trip():
    """
    Test of data scrapper.
    """
    result = scrap_trip("2022-01-31", "BORDEAUX ST JEAN", "PARIS (intramuros)")
    assert result['nhits'] > 0
