import pandas as pd
import string
import re
from functions import count_genre, count_year, remove_year,remove_extras, count_rating



def test_count_genre():

	test1 = ["action",'thriller','sci-fi', 'action']
	test2 = ["action",'thriller','sci-fi', 'action','horror']

	assert callable(count_genre)
	assert isinstance(test1,list)
	assert len(test1) == 4
	assert isinstance(test1[2], str)

	assert count_genre(test1) == {'action': 2, 'thriller': 1, 'sci-fi': 1}
	assert count_genre(test2) == {'action': 2, 'thriller': 1, 'sci-fi': 1, 'horror': 1}

def test_count_year():
	initial = [2019,2019,2011,2018,2017]
	initial2 = [2019,2019,2011]

	assert callable(count_year)
	assert isinstance(initial, list)
	assert len(initial) == 5
	assert isinstance(initial[0], int)

	assert count_year(initial) == {2019: 2, 2011: 1, 2018: 1, 2017: 1}
	assert count_year(initial2) == {2019: 2, 2011: 1}

def test_remove_extras():
	
	titles = ['Grownups ()']
	titles2 = ['Grom () days']
	titles3 = ['Grom (99) days']

	assert callable(remove_extras)
	assert len(titles) == 1
	assert isinstance(titles[0], str)

	assert remove_extras(titles) == ['Grownups ', '']
	assert remove_extras(titles2) == ['Grom ', ' days']
	assert remove_extras(titles3) == ['Grom (99) days']


def test_remove_year():
	film = ['Grownups (2010)']
	film2 = ['Grownups (2010)','Grownups 2 (2013)']

	assert callable(remove_year)
	assert len(film) == 1

	assert isinstance(film[0], str)
	assert remove_year(film) == ['Grownups ()']
	assert remove_year(film2) == ['Grownups ()', 'Grownups  ()']

def test_count_rating():
	rating = ['7.8','9.2','7.8','6.6']
	rating2 = ['7.8','9.2','7.8','6.6',6.6]

	assert callable(count_rating)
	assert isinstance(rating, list)
	assert len(rating) == 4
	assert isinstance(rating[0], str)
	assert isinstance(rating2[4], float)


	assert count_rating(rating) == {'7.8': 2, '9.2': 1, '6.6': 1}
	assert count_rating(rating2) == {'7.8': 2, '9.2': 1, '6.6': 1, 6.6: 1}
