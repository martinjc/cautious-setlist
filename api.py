#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests

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

def get_setlists_for_artist(artist_mbid):

    endpoint = '/1.0/artist/%s/setlists' % artist_mbid
    url = URL_ROOT + endpoint
    r = requests.get(url, headers=HEADERS)
    return r.json()


def main():

    artists = search_for_artist('weezer')
    artist = artists['artist'][0]
    pprint_json(artist)
    artist_mbid = artist['mbid']

    setlists = get_setlists_for_artist(artist_mbid)
    pprint_json(setlists)

if __name__ == '__main__':
    main()
