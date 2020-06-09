"A collection of the functions used in my project"
def count_genre(genre1):
    count = {} 
    #new dictionary for the count to be updated to
    for i in genre1: 
        # loops through and counts each specific genre
        count[i] = count.get(i, 0) + 1
    return count

def count_year(initial):
    count = {} 
    # creates empty dictionary for values
    for i in initial: 
        # counts how many times a year is present and stores its value
        count[i] = count.get(i, 0) + 1
    return count

import re
def remove_year(titles):
    #defining a pattern of numbers we are looking for
    pattern = '[0-9]'
    # looping through titles and replacing all numbers with a blank space.
    updated = [re.sub(pattern, '', i) for i in titles] 
    return updated

def remove_extras(new_titles):
    #function called to remove extra parenthesis
    str1 = ''.join(new_titles)
    # creates new string that splits previous at parenthesis
    temp = str1.split('()')
    return temp

def count_rating(rating):
    count = {} 
    # creates an empty dictionary
    for i in rating: 
        # counts each individual occurence of a rating per film
        count[i] = count.get(i, 0) + 1
    return count