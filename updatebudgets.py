from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import json

with open("imdb_output.json", "r") as f:
    movies = json.load(f)

with open("movie_budget.json", "r") as f:
    budgets = json.load(f)

titles = {}
titlesList = []
for id, movie in enumerate(budgets):
	titles[movie['movie_name']]= id
	titlesList.append(movie['movie_name'])


newMovies = []
for id, movie in enumerate(movies):
	#find the closest match
	match = process.extractOne(movie['movie_title'], titlesList)
	result = match[0]

	if match[1] > 90:
		#get the proper budget data
		budget_data = budgets[titles[result]]
		movie['release_date'] = budget_data['release_date']
		movie['worldwide_gross'] = budget_data['worldwide_gross']
		movie['production_budget'] = budget_data['production_budget']
		newMovies.append(movie)

with open('imdb_output_budget.json', 'w') as fp:
    json.dump(newMovies, fp)