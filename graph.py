import networkx as nx

from collections import defaultdict

def init_graph():
    return nx.Graph()


def add_song_to_graph(G, song, set_type):
    name = song['name']
    cover = False
    if song.get('cover'):
        cover = True
    if G.has_node(name):
        if G.node[name].get(set_type):
            count = G.node[name][set_type]
        else:
            count = 0
        if not cover:
            G.add_node(name, {set_type: count+1})
        else:
            G.add_node(name, {set_type: count+1, 'cover': True})
    else:
        if not cover:
            G.add_node(name, {set_type: 1})
        else:
            G.add_node(name, {set_type: 1, 'cover': True})

def add_edge_to_graph(G, this_song, that_song):
    if G.has_edge(this_song, that_song):
        if G[this_song][that_song].get('count'):
            count = G[this_song][that_song]['count']
        else:
            count = 0
        G.add_edge(this_song, that_song, {'count': count+1})
    else:
        G.add_edge(this_song, that_song, {'count': 1})




def add_setlist_to_graph(G, setlist):
    for song_set in setlist:
        if song_set.get('encore'):
            for song in song_set['song']:
                add_song_to_graph(G, song, 'encore')
        else:
            for song in song_set['song']:
                add_song_to_graph(G, song, 'set')

    songs = []
    for song_set in setlist:
        for song in song_set['song']:
            songs.append(song['name'])

    for this_song in songs:
        for that_song in songs:
            if not this_song == that_song:
                add_edge_to_graph(G, this_song, that_song)


    return G
