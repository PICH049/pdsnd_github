import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True:
          city = input('\nPlease enter the City you are interested in. Choose out of: chicago,new york city or washington.\n').lower()
          if city in ('chicago','new york city','washington'):
            break

    #get user input for month (all, january, february, ... , june)
    while True: 
           month = input('\nPlease enter the month you are interested in. Choose out of: all or january, february, ... , june...Check your spelling!\n').lower()
           if month in ('all', 'january', 'february','march','april','may','june','july','august','september','october','november','december'):
            break
            
    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
           day = input('\nPlease enter the day of the week you are interested in. Choose out of: all, monday, tuesday, ... sunday...Check your spelling!\n').lower()
           if day in ('all', 'monday', 'tuesday','wednesday','thursday', 'friday', 'saturday','sunday'):
            break

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
    
    
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
      df = df[df['month'].str.startswith(month.title())]
      
    if day != 'all':
       df = df[df['day'].str.startswith(day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    #display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print('The most common month is ', most_common_month)

    #display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    most_common_day = df['day'].mode()[0]
    print('The most common day is ', most_common_day)

    #display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is ', most_common_hour)
  
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is ', most_common_start) 

    #display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is ', most_common_end)

    #display most frequent combination of start station and end station trip
    common_trip = 'from' + df['Start Station'] +" to "+ df['End Station'].mode()[0]
    print('The most frequent combination of start station and end station trip is ', common_trip)

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The total travel time is ', total_trip_duration)    

    #display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('These are all the users types:\n', user_types)

    #display counts of gender
    try:
        gender_types = df['Gender'].value_counts().to_frame()
        print('This is the gender split of all users: \n', gender_types)
        #display earliest, most recent, and most common year of birth
        print('The earliest year of birth is ', df['Birth Year'].min())
        print('The most recent year of birth is ', df['Birth Year'].max())
        print('The most common year of birth is ', df['Birth Year'].mode()[0])
    except:
        print('There are no gender specifications for the city Washington!')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input("Do you want to see 5 rows of data? Enter yes or no? ").lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you want to see 5 more rows of data? Enter yes or no? ").lower()
        
    return df

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
main()
