import time
import pandas as pd
import numpy as np
import json

CITY_LIST = {
            'chicago': 'chicago.csv',
             'new york': 'newyork.csv',
             'washington': 'washington.csv'
             }

def get_userinputs():
    """
    User will choose a city, month, and day to analyze.

    Specifically:
        1. city - name of the city to analyze
        2. month - name of the month to filter by, or "all"
        to apply no month filter
        3. day - name of the day of week to filter by, or "all"
        to apply no day filter
    """

    print('\n______________________________***Bikeshare***______________________________')
    print(' Wellcome! Let\'s explore some bike-sharing data of some US cities! '.center(70, '='))
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = None
    city_options = ['chicago', 'new york', 'washington']
    while city not in city_options:
        city = input("\nCity of your choice\n[ Chicago, New York or Washington ] : ").lower()

    # get user input for month (all, january, february, ... , june)
    month = None
    month_options = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in month_options:
        month = input("\nMonth of your choice\n[ all, january, february,"
                      "march, april, may, or june ] : ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    day_options = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    while day not in day_options:
        day = input("\nDay of the week\n['all', 'monday', ...., 'sunday'] : ").lower()

    print('-'*70, '\n')
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        1. city - name of the city to analyze
        2. month - name of the month to filter by, or "all" to apply no month filter
        3. day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        dataFrame - Pandas DataFrame containing city data filtered by month and day
    """
    print("\n Filters applied : [ {}, {}, {}] ".format(city, month, day).center(78, '*'))
    print()

    # load data file into a dataframe
    dataFrame = pd.read_csv(CITY_LIST[city])

    # convert Start Time column to datetime type
    dataFrame['Start Time'] = pd.to_datetime(dataFrame['Start Time'])

    # create new columns from month and day of week from Start Time extracted
    dataFrame['month'] = dataFrame['Start Time'].dt.month
    dataFrame['day_of_week'] = dataFrame['Start Time'].dt.day_name()

    # filter by month if available
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
       
        dataFrame = dataFrame[dataFrame['month'] == month]

    # filter by day of week if available
    if day != 'all':
        # filter by day of week to create the new dataframe
        dataFrame = dataFrame[dataFrame['day_of_week'] == day.title()]

    return dataFrame