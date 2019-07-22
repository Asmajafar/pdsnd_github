import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new_york_city', 'washington']


MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']


DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
'thursday', 'friday', 'saturday' ]


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

    while True:
       city = input('Which city do you want to explore Chicago, new_york_city or Washington? \n ').lower()
       if city in CITIES:
          break 
       else:
           print("Oops! Looks like you did'n chose correctly please try again \n ")

            # TO DO: get user input for month (all, january, february, ... , june)

    while True:        
       month = input(str('chose month to explore or all to show january, february, march, april, may, june) \n ').lower()) 
       if month in MONTHS or month == 'all':
          break 
       else:
           print("Oops! Looks like you did'n chose correctly please try again \n ")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
       day = input(str('chose day to explore sunday, monday, tuesday, wednesday, thursday, friday, saturdayor or all \n ').lower())
       if day in DAYS or day == 'all':
          break 
       else:
           print("Oops! Looks like you did'n chose correctly please try again \n ")

 
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
    df['hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
   

    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]

    print('Most Popular start month:', popular_month)

    # TO DO: display the most common day of week

    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]

    print('Most Popular start day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel) 

    # TO DO: display mean travel time

    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("Counts of user types:\n")

    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    
    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)
    else:
        print('Column does not exist')


    if 'Birth Year' in df.columns:
        user_stats_birth(df)
    else:
        print('Column does not exist')


    print("\nThis took %s seconds." % (time.time() - start_time))

    # TO DO: Display counts of gender

def user_stats_gender(df):

    print("Counts of gender:\n")

    gender_counts = df['Gender'].value_counts()

    # iteratively print out the total numbers of genders 

    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth

def user_stats_birth(df):

    start_time = time.time()

    birth_year = df['Birth Year']
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)

    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)

    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5

    for i in range(0, row_length, 5):
        
        yes = input('\n do you want to see more 5 lines of raw data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 

        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:

            # pretty print each user data
            
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)         
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
