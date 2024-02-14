# customlib.py
#
# Author: Tayana Roychowdhury
#
# Custom library for final project.

import csv
from collections import deque
from matplotlib import pyplot as plt
import numpy as np

class Country:
    def __init__(self, name, stats=None):
        self.name = name
        if stats == None:
            stats = {}
        self.stats = stats

    def getName(self):
        return self.name

    def getStats(self):
        return self.stats

    def setStats(self, stats):
        self.stats = stats

    # returns the years that have data in the stats dict
    def getYears(self):
        return self.stats.keys()

class CountryGraphs(Country):
    # makes line graph with all years on x-axis and plots suicides/100k people
    # of the different age groups of the specified sex
    def makeLineGraphAllAges(self, sex):
        stats = self.getStats()
        years = list(self.getYears())
        ages_5_to_14 = []
        ages_15_to_24 = []
        ages_25_to_34 = []
        ages_35_to_54 = []
        ages_55_to_74 = []
        ages_75over = []
        for year in years:
            for key in stats[year][sex].keys():
                y_value = stats[year][sex][key][1]
                if key == '5-14 years':
                    ages_5_to_14.append(y_value)
                elif key == '15-24 years':
                    ages_15_to_24.append(y_value)
                elif key == '25-34 years':
                    ages_25_to_34.append(y_value)
                elif key == '35-54 years':
                    ages_35_to_54.append(y_value)
                elif key == '55-74 years':
                    ages_55_to_74.append(y_value)
                elif key == '75+ years':
                    ages_75over.append(y_value)
                    

        fig, ax = plt.subplots()
            
        ax.plot(years, ages_5_to_14, label='5-14 years')
        ax.plot(years, ages_15_to_24, label='15-24 years')
        ax.plot(years, ages_25_to_34, label='25-34 years')
        ax.plot(years, ages_35_to_54, label='35-54 years')
        ax.plot(years, ages_55_to_74, label='55-74 years')
        ax.plot(years, ages_75over, label='75+ years')

        ax.set_yticks(np.arange(0, 250, 50))
        ax.set_yticklabels(['0', '50', '100', '150', '200'])
        ax.set_xlabel('Years')
        ax.set_ylabel('Suicides/100K pop')
        ax.set_title('Suicide rates among '+sex+'s'+' in '+self.name)
        ax.legend()
        
        plt.tight_layout()
        plt.show()

    # makes line graph with all years on x-axis and plots suicides/100k people
    # for one age group in both sexes
    def makeLineGraphOneAge(self, age):
        stats = self.getStats()
        years = list(self.getYears())
        male_data = []
        female_data = []
        pop_male = []
        pop_female = []
        for year in years:
            male_rate = stats[year]["male"][age][1]
            male_data.append(male_rate)
            mpop = stats[year]["male"][age][0]
            pop_male.append(mpop)

            female_rate = stats[year]["female"][age][1]
            female_data.append(female_rate)
            fpop = stats[year]["female"][age][0]
            pop_female.append(fpop)


        fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
        ax1.plot(years, male_data)
        ax1.plot(years, female_data)
        ax1.set_yticks(np.arange(0, 250, 50))
        ax1.set_yticklabels(['0', '50', '100', '150', '200'])
        ax1.set_ylabel('Suicides/100K pop')
        ax1.legend(labels=['Female rate','Male rate'])
        ax1.set_title('Suicide rates in '+self.name+' for ages '+age)

        ax2.plot(years, pop_male)
        ax2.plot(years, pop_female)
        ax2.set_xlabel('Years')
        ax2.set_ylabel('Population')
        ax2.set_yscale('log')
        ax2.legend(labels=['Female demographic population','Male demographic population'])
        
        plt.tight_layout()
        plt.show()
        
    
# Prints out the names of the countries/regions beginning with letter. 
def showCountries(c):
    with open('finaldata.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        countries = []
        c = c.capitalize()
        for line in csv_reader:
            if line['country'].startswith(c):
                if line['country'] not in countries:
                    countries.append(line['country'])
        if not countries:
            print("There are no recorded data for countries beginning with that letter.")
        else:
            for name in countries:
                print(name)

# Checks to see if country/region is in the file. 
def isPresent(country):
    with open('finaldata.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            if line["country"] == country:
                return True
        return False

# Exports csv file containing raw data for countries.
def exportData(queue, file_name):
    with open('finaldata.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Store the rows in a list
        rows = list(csv_reader)

        with open(file_name, 'w', newline='') as new_file:
            fieldnames = csv_reader.fieldnames
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            while queue:
                country_name = queue.popleft()
                for line in rows:  # Iterate over the stored rows
                    if line['country'] == country_name:
                        csv_writer.writerow(line)

# Returns a nested dictionary of all the stats for a country/region.
def makeStats(country_name, file_name='finaldata.csv'):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = [row for row in csv_reader if row['country'] == country_name]
        stats = {}
        for row in rows:
            year = int(row['year'])
            sex = row['sex']
            age = row['age']
            gdp = int(row['gdp_per_capita_dollars'])
            l = [row['population'], row['suicides_per_100k'], row['generation']]
            stats.setdefault(year, {})
            stats[year].setdefault(sex, {})
            stats[year].setdefault('gdp', gdp)
            stats[year][sex].setdefault(age, l)
        return(stats)  
                   
    
##if __name__ == "__main__":
##    stats = makeStats("United States")
##    us = CountryGraphs("United States", stats)
##    us.makeLineGraphOneAge("15-24 years")
    
    
    
    

    
