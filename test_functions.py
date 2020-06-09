import pandas as pd
import string
import re
from functions import count_genre, count_year, remove_year,remove_extras, count_rating

file = pd.read_csv("IMDB_Titles.csv")
titles = file.Title.unique()
initial = list(file['Year'])
genre1 = list(file['Genre'])
rating = list(file['Rating (Of 10)'])


def count_genre(genre1):

	test1 = ["action",'thriller','sci-fi', 'action']
	assert callable(count_genre)
	assert isinstance(genre1,list)
	assert len(genre1) == 100
	assert isinstance(genre1[2], str)

	assert count_genre(test1) == {'action': 2, 'thriller': 1, 'sci-fi': 1}

def count_year(initial):
	assert callable(count_year)
	assert isinstance(initial, list)
	assert len(initial) == 100
	assert isinstance(initial[0], int)

	assert count_year([2019,2019,2011,2018,2017]) == {2019: 2, 2011: 1, 2018: 1, 2017: 1}

def remove_extras(titles):
	assert callable(remove_extras)
	assert len(titles) == 100
	assert isinstance(titles[0], str)

	assert remove_extras(['Grownups ()']) == ['Grownups ', '']
	assert remove_extras(['Grom () days']) == ['Grom ', ' days']
	assert remove_extras(['Grom (99) days']) == ['Grom (99) days']


def remove_year(titles):
	assert callable(remove_year)
	assert len(titles) == 100

	assert isinstance(titles[5], str)
	assert remove_year(['Grownups (2010)']) == ['Grownups ()']

def count_rating(rating):
	assert callable(count_rating)
	assert isinstance(rating, list)
	assert len(rating) == 100
	assert isinstance(rating[0], float)

	assert count_rating(['7.8','9.2','7.8','6.6']) == {'7.8': 2, '9.2': 1, '6.6': 1}
	assert count_rating(['7.8','9.2','7.8','6.6',6.6]) == {'7.8': 2, '9.2': 1, '6.6': 1, 6.6: 1}
