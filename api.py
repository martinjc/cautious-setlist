#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests

from graph import *
from _credentials import *

URL_ROOT = 'https://api.setlist.fm/rest/'

HEADERS = {
    'accept': 'application/json',
    'x-api-key': API_KEY
}

def pprint_json(json_obj):
    print(json.dumps(json_obj, sort_keys=True, indent=4, ensure_ascii=False))


def search_for_artist(artist_name):

    endpoint = '1.0/search/artists'
    payload = {
        'artistName': artist_name
    }
    url = URL_ROOT + endpoint
    r = requests.get(url, headers=HEADERS, params=payload)
    return r.json()

def get_setlists_for_artist(artist_mbid, page=1):

    endpoint = '/1.0/artist/%s/setlists' % artist_mbid
    url = URL_ROOT + endpoint

    payload = {
        'p': page
    }

    r = requests.get(url, headers=HEADERS, params=payload)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


def main():

    artists = search_for_artist('weezer')
    artist = artists['artist'][0]
    artist_mbid = artist['mbid']

    G = init_graph()

    for p in range(1, 20):
        setlists = get_setlists_for_artist(artist_mbid, p)
        if not setlists is None:
            for setlist in setlists['setlist']:
                date = setlist['eventDate']
                sets = setlist['sets']['set']
                add_setlist_to_graph(G, sets)

    print(G.nodes(data=True))
    print(G.edges(data=True))

    nx.write_gml(G, 'test.gml')

if __name__ == '__main__':
    main()
