from pyvis.network import Network
import json


def read_json(fname, verbose=False):
    with open(fname, 'r') as f:
        data = json.load(f)
    return data

movie_db = read_json('movie_db.json')

g = Network(height="1050px", width="100%", bgcolor="#222222", font_color="white")

for i, movie in enumerate(movie_db["movies"]):
	title = 'Director:' + movie['director'] if 'director' in movie.keys() else 'UNK' + " "  # @TODO create HTML separator
	title += 'Year:' + str(movie['year']) 
	if "cover" in movie.keys():
		g.add_node(i, label=movie["title"], shape = "image", image=movie["cover"], title=title)
	else:
		g.add_node(i, label=movie["title"], title=title)

for i, movie_src in enumerate(movie_db["movies"]):
	for j, movie_dst in enumerate(movie_db["movies"]):
		if i != j and movie_src['year'] == movie_dst['year']:
			print('Build new edge', movie_src['title'], movie_dst['title'])
			g.add_edge(i, j, value=0.5)
		elif i != j and 'director' in movie_src.keys() and 'director' in movie_dst.keys() and movie_src['director'] == movie_dst['director']:
			g.add_edge(i, j, value=1)

g.toggle_drag_nodes(True)
g.toggle_physics(True)
g.show("movie-visu.html")