# mainprog.py
# Author: Tayana Roychowdhury
# Main program for final Python project.

import customlib
from collections import deque

print("Welcome to MentalMap, a user-friendly tool and database allowing you" \
        " to view and visualize mental health statistics for places around the world.")
print("Currently, we have statistics focusing on suicide rates.")
print("\n")
print("To see the names of the countries or regions we have data for, enter" \
          " a letter that the names should start with. Enter any other key to continue.")
while True:
    prompt = input("\nEnter your choice:\n>>> ")
    if prompt.isalpha():
        customlib.showCountries(prompt)
    else: 
        break

print("*" * 50)

print("Users can export raw data from our database in a csv file for any number of countries they choose." \
      " Would you like to export data?")
prompt = input("\nEnter Y or N:\n>>> ")

if prompt == "Y" or prompt == "y":
    print("Please enter the proper name of the country/region for which you want data. Enter 'd' to" \
          " remove your last choice. Enter 'done' to finish selecting.")
    queue = deque()
    while True:
        prompt = input("\nEnter your choice:\n>>> ")
        if prompt == 'done':
            break
        elif prompt == 'd':
            try:
                queue.pop()
            except:
                print("There's nothing to delete.")
        elif customlib.isPresent(prompt):
            if prompt not in queue:
                queue.append(prompt)
                print(' '.join(queue))
            else:
                print("You've already selected that.")
        else:
            print("Not a valid option.")

    print("\nWhat should the file name be?")
    file_name = input("Enter a name that ends with '.csv':\n>>> ")
    print("\nExport data?")
    prompt = input("Enter Y or N:\n>>> ")
    if prompt == "Y" or prompt == "y":
        try:
            customlib.exportData(queue, file_name)
        except:
            print("Oops, there was a problem.")
        else:
            print("Data successfully exported.")

print("*" * 50)

print("Our data visualization tool allows you to view different preset graphs" \
      " based on our data.")
print("Enter 'S' to visualize data for a single country.\nEnter any other key to quit.")

prompt = input("\nEnter your choice:\n>>> ")
if prompt == 'S' or prompt == 's':
    print("\nWhich country/region would you like to see graphs for?")
    country_name = input("Enter a proper name:\n>>> ")
    if customlib.isPresent(country_name):
        stats = customlib.makeStats(country_name)
        country = customlib.CountryGraphs(country_name, stats)
        print("Would you like to see data comparing ages or sexes?" \
              " Enter 'a' for the first graph or 's' for the second graph.")
        prompt = input("\nEnter your choice:\n>>> ")
        if prompt == 's' or prompt == 'S':
            prompt = input("\nEnter 'a' for '5-14 years', 'b' for '15-24 years', 'c' for '25-34 years',"\
                           " 'd' for '35-54 years', 'e' for '55-74 years', or 'f' for '75+ years':\n>>> ")
            if prompt == 'A' or prompt == 'a':
                country.makeLineGraphOneAge('5-14 years')
            elif prompt == 'B' or prompt == 'b':
                country.makeLineGraphOneAge('15-24 years')
            elif prompt == 'C' or prompt == 'c':
                country.makeLineGraphOneAge('25-34 years')
            elif prompt == 'D' or prompt == 'd':
                country.makeLineGraphOneAge('35-54 years')
            elif prompt == 'E' or prompt == 'e':
                country.makeLineGraphOneAge('55-74 years')
            elif prompt == 'F' or prompt == 'f':
                country.makeLineGraphOneAge('75+ years')
        elif prompt == 'a' or prompt == 'A':
            prompt = input("\nEnter 'male' or 'female':\n>>> ")
            if prompt == 'male':
                country.makeLineGraphAllAges('male')
            else:
                country.makeLineGraphAllAges('female')
            

print("That's all we have right now. Thanks for using MentalMap.")

    
    

    
                    


