import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities_name={"chicago" , "new york city" , "washington"}
months_name={"january", "february", "march", "april", "may", "june","all"}
days_name={"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday","all"}    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input('Would you like to see data for chicago, new york city or washington ').lower()
    while city not in cities_name :
        city= input('Please choose one of these cities chicago, new york city or washington ').lower()
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month= input('write what month you want to explore , january, february, march, april, may, june or "all" for all month ').lower()
    while month not in months_name :
        month= input('Please choose one of these months january, february, march, april, may, june or "all" for all month ').lower() 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)    
    day= input('write what day you want to explore , monday, tuesday, wednesday, thursday, friday, saturday, sunday or "all" for all days ').lower()
    while day not in days_name :
        day= input('Please choose one of these days monday, tuesday, wednesday, thursday, friday, saturday, sunday or "all" for all days').lower()
    

    print('-'*40)
    return city, month, day


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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
 
    return df    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('Most Common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print('Most Common Hour:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Common start station is :', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most Common end station is :', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End stations'] = df['Start Station'] + df['End Station']
    common_start_end_station = df['Start End stations'].value_counts().idxmax()  
    print('most frequent combination of start station and end station trip',common_start_end_station)   
 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time is ',mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    if city == 'new york city' or city == 'chicago':
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        counts_user_types=df['User Type'].value_counts()
        print('counts of user types is ')
        print(counts_user_types.to_string())

        # TO DO: Display counts of gender
        counts_gender=df['Gender'].value_counts()
        print('counts of gender is ')
        print(counts_gender.to_string())

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        print('earliest of birth is ',earliest)

        recent = int(df['Birth Year'].max())
        print('recent of birth is ',recent)

        common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print('most common year of birth is ',common_year_of_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    else :
        print("user data were not found")
        
def display_raw_data(df):
    """ Your docstring here """
    i = 0
    raw = input("would you like to display raw data . Please enter only 'yes' or 'no'  ") # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i: i + 5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("would you like to display the next 5 row . Please enter only 'yes' or 'no'") # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

        
def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
	""" to chose if the user want to restart or not"""
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
