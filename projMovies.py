# Bryon Garcia
# CSC-110 - Fall 2023
# Final Project
# 12-3-23



# program Title: Movies Data

# project Description:

# this code will read into a large data file with information about movies that were released between 2006 and 2016 and display information requested by the user.
# The program will allow the user to get answers to various questions about the movies in the data file.


# l =[] or l is my list of index's 

# function name: open_file
# arguments: nonw
# return: movie_file
# description: asks the user to input the file and use that file later on if it is the wrong file it will give an error
def open_file():
    good_file = False
    while good_file == False:
        fname = input("Please enter a file name: ")
        # Begin exception handling
        try:
            # Try to open the file with the given name
            movie_file = open(fname, 'r')
            good_file = True
        except IOError:
            # If file name is not valid IOError exception is raised
            print("Invalid file name try again...")
    return movie_file

# function name: get_movies
# arguments: none
# return: title_list, genre_list, director_list, years_list, run_time_list, revenue_list
# description: takes all the lists in the file and appends it to an empty list so it can be used later in the code
def get_movies():
    infile = open_file()
    title_list = []
    genre_list = []
    director_list = []
    years_list = []
    run_time_list = []
    revenue_list = []
    line = infile.readline()
    for line in infile:
        line = line.strip()
        title, genre, director, years, runtime, revenue = line.split(',')
        title_list.append(str(title))
        genre_list.append(str(genre))
        director_list.append(str(director))
        years_list.append(int(years))
        run_time_list.append(int(runtime))
        revenue_list.append(float(revenue))
   
    infile.close()
    return title_list, genre_list, director_list, years_list, run_time_list, revenue_list

# function name: getChoice
# arguments: none
# return: choice
# description: This function displays the menu of choices for the user. It reads in the user's choice and returns it as an integer, along with error checking the choice
def getChoice():
    print("")
    print("Please choose one of the following options:")
    print("1 -- Find all films made by a specified director")
    print("2 -- Find the highest grossing film made in a specific year")
    print("3 -- Find all films made in a given year range in a specified genre")
    print("4 -- Search for a film by title")
    print("5 -- Find average runtime of films with higher revenue than specified value")
    print("6 -- Sort all lists by revenue and write the results to a new file")
    print("7 -- Quit")
    OK = False
    while OK == False:
        try:
            choice = int(input("Choice ==> "))
            if choice in range(1, 8):
                OK = True
            if choice not in range(1, 8):
                print("Choice must be between 1 and 7")
        except ValueError:
            print("Invalid entry - Try again")
    print("")
    
    return choice

# function name: print_all
# arguments: l, title_list, genre_list, director_list, years_list, run_time_list, revenue_list
# return: none
# description: prints everything all the lists and also lines everything up 
def print_all(l, title_list, genre_list, director_list, years_list, run_time_list, revenue_list):
    print("TITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
    for i in l:
        print(title_list[i].ljust(45), genre_list[i].ljust(35), director_list[i].ljust(24), str(years_list[i]).ljust(8),str(run_time_list[i]).ljust(8), ("$"+str(revenue_list[i])).rjust(12))
    return

# function name: find_director
# arguments: title_list, genre_list, director_list, years_list, run_time_list, revenue_list, pick
# return: l
# description: finds the director if it is in the list then it gets appended to an empty list
def find_director(director_list, pick):
    l = []
    for i in range(len(director_list)):
        if pick == (director_list[i]):
            l.append(i)
    return l


# function name: highest_grossing_in_year
# arguments: revenue_list, years_list, year_1
# return: l
# description: finds the highest grossing revenue in a year and appends it to an empty list
def highest_grossing_in_year(revenue_list, years_list, year_1):
    high = 0
    high_index = 0
    l = []
    for i in range(len(revenue_list)):
        if years_list[i] == int(year_1):
            if high < revenue_list[i]:
                high = revenue_list[i]
                high_index = i
    l.append(high_index)
                

    return l



# function name: search_title
# arguments: title_list, genre_list, director_list, years_list, run_time_list, revenue_list, search
# return: l
# description: goes though the title list to find a speifcic title
def search_title(title_list, genre_list, director_list, years_list, run_time_list, revenue_list, search):
    left = 0
    # right side of the list                
    right = len(title_list) - 1        
    while right >= left:
        # find the middle of the list
        m = (left + right) // 2
        if search == title_list[m]:
            title = (title_list[m])
            genre = (genre_list[m])
            director = (director_list[m])
            year = (years_list[m])
            runtime = (run_time_list[m])
            revenue = (revenue_list[m])
            return m
        elif search < title_list[m]:
            right = m - 1
        else:
            left = m + 1
        
    return []

# function name: get_year
# arguments: years_list
# return: year1
# description: ask the user for the years and if the year is in the list then it gets returned if not there are a set of errors for each outcome
def get_year(years_list):
    OK = False
    while OK == False:
        try:
            year1 = int(input("Enter year: "))
            if year1 in years_list:
                OK = True
            if year1 not in years_list:
                print("Year out of range, must be between 2006 and 2016")
        except ValueError:
            print("Invalid entry - Try again")

    return year1
              
# function name: get_valid_year1
# arguments: years_list
# return: year1
# description: ask the user for the year 1 and if the year is in the list then it gets returned if not there are a set of errors for each outcome, it also checks to see if the years the user inputs are in the range of 2006 and 2016        
def get_valid_year1(years_list):
    year1_valid = False
    while year1_valid == False:
        try:
            year1 = int(input("Year1: "))
            if year1 in years_list:
                year1_valid = True
            else:
                print("Year out of range, must be between 2006 and 2016")
        except ValueError:
            print("Invalid entry - Try again")
    return year1

# function name: get_valid_year1
# arguments: years_list
# return: year2
# description: ask the user for the year2 and if the year is in the list then it gets returned if not there are a set of errors for each outcome, it also checks to see if the years the user inputs are in the range of 2006 and 2016  
def get_valid_year2(years_list):
    year2_valid = False
    while year2_valid == False:
        try:
            year2 = int(input("Year2: "))
            if year2 in years_list:
                year2_valid = True
            else:
                print("Year out of range, must be between 2006 and 2016")
        except ValueError:
            print("Invalid entry - Try again")
    return year2

# function name: valid_years
# arguments: years_list
# return: year1, year2
# description: calls get_vaild_year1 & get_vaild_year2 it asks the user for the years and if the years is in the list then it gets returned if not there are a set of errors for each outcome, it also checks to see if the years the user inputs are in the range of 2006 and 2016 and if year 2 comes before year1   
def valid_years(years_list):
    year1 = get_valid_year1(years_list)
    year2 = get_valid_year2(years_list)
    while year2 <= year1:
        print("Second year should be after first year - try again")
        year1 = get_valid_year1(years_list)
        year2 = get_valid_year2(years_list)
    return year1, year2

# function name: get_genre
# arguments: genre_list
# return: genre
# description: the user inputs the genre error checks the genre
def get_genre(genre_list):
    OK = False
    while OK == False:
        try:
            genre = input("Enter genre: ")
            if genre in genre_list:
                OK = True
            else:
                print("Invalid entry - Try again")
        except ValueError:
            print("Invalid entry - Try again")
    return genre


# function name: year_genre_filter
# arguments: years_list, genre_list
# return: year_genre
# description: takes the two list and if the years are in the valid_years function and the get_genre functuion it goes through the loop and gets appened to a new list    
def year_genre_filter(years_list, genre_list):
    year1, year2 = valid_years(years_list)
    genre = get_genre(genre_list)
    year_genre = []
    for i in range(len(genre_list)):
        if genre in genre_list[i] and year1 <= years_list[i] <= year2:
            year_genre.append(i)
    
    return year_genre

# function name: average_run_time_with_revenue
# arguments: run_time_list, revenue_list, limit
# return: average (float)
# description: goes though the lenth of the run_time_list and if the index of the revenue_list is greater the revenue limit then the total is the index of the run_time_list then uses that to get the avarage 
def average_run_time_with_revenue(run_time_list, revenue_list, limit):
    total = 0
    x = 0
    for i in range(len(run_time_list)):
        if revenue_list[i] > float(limit):
            total = total + run_time_list[i]
            x = x + 1
    if x == 0:
        average = 0
    else:
        average = total / x
    return average

# function name: get_limit
# arguments: run_time_list, revenue_list
# return: limit(float)
# description: the user inputs the limit error checks the limit and ends it with a boolean, also calling average_run_time_with_revenue function.
def get_limit(run_time_list, revenue_list):
    limit = 0
    valid_input = False
    if valid_input == False:
        limit_input = input("Enter revenue limit (millions): $")
        try:
            limit = float(limit_input)
            valid_input = True
        except ValueError:
            print("Invalid entry, try again")
        if valid_input:
            if limit >= 760.51:
                print("No films have revenue higher than $ {:.2f} million.".format(limit))
                valid_input = True  
            elif limit < 760.51:
                average = average_run_time_with_revenue(run_time_list, revenue_list, limit)
                print("The average runtime for films with revenue higher than $ {:.2f} million is {:.2f} minutes.".format(limit, average))
    return limit

# function name: insertionSort
# arguments: title_list, genre_list, director_list, years_list, run_time_list, revenue_list
# return: title_list, genre_list, director_list, years_list, run_time_list, revenue_list
# description: sorts all the lists 
def insertionSort(title_list, genre_list, director_list, years_list, run_time_list, revenue_list):
    for i in range(1, len(revenue_list)):
        save = revenue_list[i]
        save_1 = title_list[i]
        save_2 = genre_list[i]
        save_3 = director_list[i]
        save_4 = years_list[i]
        save_5 = run_time_list[i]
        j = i
        while j > 0 and revenue_list[j - 1] > save:
            # comparison
            revenue_list[j] = revenue_list[j - 1]
            title_list[j] = title_list[j - 1]
            genre_list[j] = genre_list[j - 1]
            director_list[j] = director_list[j - 1]
            years_list[j] = years_list[j - 1]
            run_time_list[j] = run_time_list[j - 1]
            j = j - 1
	    # swap
        revenue_list[j] = save
        title_list[j] = save_1
        genre_list[j] = save_2
        director_list[j] = save_3
        years_list[j] = save_4
        run_time_list[j] = save_5
        
        
        
    return title_list, genre_list, director_list, years_list, run_time_list, revenue_list

# function name: write_file
# arguments: title_list, genre_list, director_list, years_list, run_time_list, revenue_list
# return: none
# description: allows the user to input a new file name that will be saved into their files
def write_file(title_list, genre_list, director_list, years_list, run_time_list, revenue_list):
    out_fname = "movies-sorted-rev.csv"
    out_file = open(out_fname,'w')
    for i in range(0,len(revenue_list)):
        out_file.write(str(title_list[i]) + "," + str(genre_list[i]) + "," + str(director_list[i]) + "," + str(years_list[i]) + "," + str(run_time_list[i]) +  "," +  str(revenue_list[i]) + "\n") 
    out_file.close()
    print("Sorted data has been written to the file:", out_fname, ".")
    return

# function name: main
# arguments: none
# return: none
# description: runs all the functions  
def main():    
    # Call the function to get the data from the data file and store the results in three lists
    title_list, genre_list, director_list, years_list, run_time_list, revenue_list = get_movies()
    choice = getChoice()
    l = []
    while choice != 8:
        if choice == 1:
            # finds all flims made by a specifed director
            while (len(l) == 0):
                pick = input("Enter director: ")
                l = find_director(director_list, pick)
                if (len(l)) == 0:
                    print("Invalid entry - Try again")
                else:
                    print("The films that meet your criteria are: ")
                    print_all(l, title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
            choice = getChoice()
        elif choice == 2:
            #finds the highest grossing film made in a specific year
            year1 = get_year(years_list)
            l = highest_grossing_in_year(revenue_list, years_list, year1)
            if (len(l)) == 0:
                print("Invalid entry - Try again")
            else:
                print("The film that meets your criteria is: ")
                print_all(l, title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
            choice = getChoice()
        elif choice == 3:
            # finds all flims made in a given year range in a specified genre
            print("Enter year range to search (oldest year first)")
            l = year_genre_filter(years_list, genre_list)
            print("The films that meet your criteria are: ")
            print_all(l, title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
            choice = getChoice()
        elif choice == 4:
            #search for a flim by title(sorted by title)
            search = input("Enter title: ")
            l = search_title(title_list, genre_list, director_list, years_list, run_time_list, revenue_list, search)
            if not l:
                print("No such film exists.")
            else:
                print("The film that meets your criteria is: ")
                print_all([l], title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
            choice = getChoice()
        elif choice == 5:
           # finds the average runtime of films with revenue higher than a specified value
            limit = get_limit(run_time_list, revenue_list)
            average = average_run_time_with_revenue(run_time_list, revenue_list, float(limit))
            
            # Call the function to find the shows with the score higher than a certain movie
            # Print the result that was returned by the function
            choice = getChoice()
        elif choice == 6:
            # sorts all lists by revenue and write the results to new file
             title_list, genre_list, director_list, years_list, run_time_list, revenue_list = insertionSort(title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
             write_file(title_list, genre_list, director_list, years_list, run_time_list, revenue_list)
             choice = getChoice()
             # Call the function to sort list by year in new file
        elif choice == 7:
            print("Good-bye")
            choice = 8
            
            
        else:
            print("Choice must be between 1 and 7")
            choice = getChoice()
            

#Bryon Garcia
#class csc 110 hw 1
#due date 9-7-23

import math
a = 8
b = 3
c = 5


z = (2 * a - 3 * b / 8 + 42 / a ** 2 - b ** 2 * 2 / a + c / 6 / b)

print (z)