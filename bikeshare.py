import time
import pandas as pd
import numpy as np
import sys

# from itertools import product
# import statistics
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


   
def get_month():
    '''get user input for month (all, january, february, ... , june)'''

    while True:
        month = input('Please Enter a full month name: e.g. "january, february, ..etc." ').title()
        if month in months: 
            break
        else:
            print("{} isn\'t a valid value for a month!".format(month))
    return month

def get_day():
    """get user input for day of week (all, monday, tuesday, ... sunday)"""
    while True:
        day = input('Please enter a day of a week e.g. saturday,...,friday ').title()
        if day in days:
            break
        else:
            print("{} isn\'t a valid value for a day!".format(day))
    return day

def concquer_time(df):
    """"
    divide start time column to month, week of day, and replaces its integer value to actual value
    Args: 
    DataFrame
    returns:
    DataFrame
    """
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    for i in range(len(months)):
        df['month'].replace(i+1, months[i], inplace=True)
    
    for i in range(len(days)):
        df['day_of_week'].replace(i, days[i], inplace=True)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        
    df = pd.read_csv(CITY_DATA[city])    
    concquer_time(df)
    df = df.loc[df['month'] == month]
    df = df[df['day_of_week'] == day]
    if city.title() == 'Washington':
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','month','day_of_week']]
    else:
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year','month','day_of_week']]
    return df.reset_index(drop=True)
    
def filter_by_month (city, month):
    df = pd.read_csv(CITY_DATA[city])
    concquer_time(df)
    df = df.loc[df['month'] == month]
    if city.title() == 'Washington':
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','month','day_of_week']]
    else:
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year','month','day_of_week']]
    return df.reset_index(drop=True)

def filter_by_day (city, day):
    df = pd.read_csv(CITY_DATA[city])
    concquer_time(df)
    df = df[df['day_of_week'] == day]
    if city.title() == 'Washington':
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','month','day_of_week']]
    else:
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year','month','day_of_week']]
    return df.reset_index(drop=True)

def load_city_data(city):
    df = pd.read_csv(CITY_DATA[city])
    concquer_time(df)
    if city.title() == "Washington":
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','month','day_of_week']]
    else:
        df = df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year','month','day_of_week']]
    return df.reset_index(drop=True)
    print('-'*40)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    most_common_month = df['month'].mode()[0]
    # display the most common day of week
    most_commond_day_of_week = df['day_of_week'].mode()[0]
    # display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]

    print("most common time of travel are:\n"
    "most common day of week {}\n"
    "most common month {}\n"
    "most common hour {}".format(most_commond_day_of_week,most_common_month,most_common_start_hour))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    count_start = pd.value_counts(df['Start Station'] == most_common_start_station)[1]
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    count_end = pd.value_counts(df['End Station'] == most_common_end_station)[1]
    
    print("most common trip station:\n"
    "Start station : {} with count : {}\n"
    "End stations : {} with count : {}\n"
    .format(most_common_start_station, count_start, most_common_end_station,count_end))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()/86400

    # display mean travel time
    average_time = df['Trip Duration'].mean()/60

    print("Total Travel Time taken is: {} (days)\n"
    "noting that the average Travel Duration is: {} (minutes)".format(total_time, average_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    user_type_counts = dict(df['User Type'].value_counts())
    print ("count of User Types: {}\n".format(user_type_counts))
    try:
        # Display counts of gender
        user_gender_counts = dict(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("Count of each Gender: {}\n"
        "Earliest year of birth: {}\n"
        "most recent year of birth: {}\n"
        "most common year of birth: {}".format(user_gender_counts,int(earliest),int(most_recent),int(most_common)))
    except KeyError:
        print("There\'s no data about gender or DOB in washington")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_statistics(df):
    """"
    this method is to prompt the user fi he wants to discover some stats about his chosen filters
    Args: df
    """
    while True:
        answer = input("Do you like to get some statistics related to your chosen filter? \n"
        "1. Yes\n"
        "2. No\n"
        "Please choose 1 or 2 \n")
    
        if answer == '1':
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            break
        elif answer == '2':
            return
        else:
            print ("Please choose either 1, or 2\n")
def show_five(df):
        """
        this method is used to show the user five rows of each chosen filters,
        and prompt him/her if they want to see more records
        Args: df
        """
        rows_count = 5
        print(df.head(rows_count))
        while True:
            get_more_records = input("\n would you like to get more records that matchs your filters? \n"
            "1. Yes\n"
            "2. No\n")
            if get_more_records == '1':
                rows_count+=5
                print(df.head(rows_count))
            elif get_more_records == '2':
                break
            else:
                print("please enter either 1, or 2\n")
   
def main():
    """"
    The main method of the script,
    it propmpt the user for his/her favourite filters, 
    then call the appropriate functions that matches the choice
    """
    while True:
        print('Hello! Let\'s explore some US bikeshare data!')  
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            city = input('Please Choose which city you want to load its data? ').lower()
            if city in CITY_DATA:
                break
            else:
                print("{} isn\'t a valid value for city name!".format(city))
        
        while True:
            answer = input("How would you like to filter your data\n"
            "1. By month\n"
            "2. By day\n"
            "3. By both\n"
            "4. None of them\n"
            "Please Choose 1, 2, 3, or 4 \n")


            if answer == '1':
                month = get_month()
                df = filter_by_month(city,month)
                print(show_five(df))
                get_statistics(df)
                break    
            elif answer == '2':
                day = get_day()
                df = filter_by_day(city,day)
                print(show_five(df))
                get_statistics(df)
                break 
            elif answer == '3':
                day = get_day()
                month = get_month()
                df = load_data(city,month,day)
                print(show_five(df))
                get_statistics(df)
                break
            elif answer == '4':
                df = load_city_data(city)
                print(show_five(df))
                get_statistics(df)
                break
            else:
                print("please choose 1, 2, 3, or 4\n")
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                main()
            elif restart.lower() == 'no':
                sys.exit(0)
            else:
                print("please enter yes or no\n")
        


try:
    main()
except KeyboardInterrupt:
    print("\n")
    sys.exit(0)
