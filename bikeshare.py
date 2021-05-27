import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':        'chicago.csv',
              'new york city':  'new_york_city.csv',
              'washington':     'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city =""
    month=""
    day=""
    months  = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days    = ['monday', 'tuesday', 'Wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


    print('\n        __o')
    print('      _-\<_')
    print('.....(_)/(_)....')

    print('\nHello! Let\'s explore some US bikeshare data! \n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA:
          city = input("\nWhat City you want to explore (Chicago, New York City, Washington)?\n >>> ").lower()

    #  get user input for month (all, january, february, ... , june)
    while month not in months:
          month = input("\nWhich month you want to explore (all, January, February, ..., June)?\n >>> ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:
          day = input("\nWhich day you want to explore (all, Monday, Tuesday, ..., Sunday)?\n >>> ").lower()

    print('\nYour filters... City:',city,' Months:',month,'Days:',day)
    print('-'*40)

    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #df["month_count"] = df['month'].count('month')
    months  = ['january', 'february', 'march', 'april', 'may', 'june']
    month_count=max((df['month'].value_counts()))
    month_number = df['month'].mode()[0]
    month   = months[month_number-1]
    print('The most common month is',month,'with a count of',month_count,'.' )

    # display the most common day of week
    day_count=max((df['day_of_week'].value_counts()))
    day = df['day_of_week'].mode()[0]
    print('The most common day is',day,'with a count of',day_count,'.' )

    #display the most common start hour
    hour_of_day_count=max((df['hour_of_day'].value_counts()))
    hour_of_day = df['hour_of_day'].mode()[0]
    print('The most common hour of day is',hour_of_day,'with a count of',hour_of_day_count,'.' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour of_day from Start Time to create new columns
    df['month']         = df['Start Time'].dt.month
    df['day_of_week']   = df['Start Time'].dt.weekday_name
    df['hour_of_day']   = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months  = ['january', 'february', 'march', 'april', 'may', 'june']
        month   = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    start_station_count=max((df['Start Station'].value_counts()))
    start_station_max = df['Start Station'].mode()[0]
    print('The most commonly used start station is',start_station_max,'with a count of',start_station_count,'.' )

    # display most commonly used end station
    end_station_count=max((df['End Station'].value_counts()))
    end_station_max = df['End Station'].mode()[0]
    print('The most commonly used end station is',end_station_max,'with a count of',end_station_count,'.' )

    # display most frequent combination of start station and end station trip
    df['trip_station']=df['Start Station']+' to '+df['End Station']
    trip_station_count=max((df['trip_station'].value_counts()))
    trip_station_max = df['trip_station'].mode()[0]
    print('The most frequent combination of start station and end station is',trip_station_max,'with a count of',trip_station_count,'.' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum(axis=0)
    seconds=total_time
    minutes=int(seconds/60)
    seconds-=minutes*60
    hours=int(minutes/60)
    minutes-=hours*60
    days=int(hours/24)
    hours-=days*24
    print('The total travel time is',total_time,'seconds. That equals: ',days,' days ',hours,' hours ',minutes,' minutes ',seconds,' seconds.')

    #display mean travel time
    mean_time=round(df['Trip Duration'].mean(axis=0),2)
    seconds=mean_time
    minutes=int(seconds/60)
    seconds-=minutes*60
    hours=int(minutes/60)
    minutes-=hours*60
    days=int(hours/24)
    hours-=days*24
    print('The mean travel time is',mean_time,'seconds. That equals: ',days,' days ',hours,' hours ',minutes,' minutes ',seconds,' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print('User Types')
    user_count=(df['User Type'].value_counts())
    print(user_count.index[0],': ',user_count[0],' counts')
    print(user_count.index[1],': ',user_count[1],' counts')

    #Display counts of gender
    if 'Gender' in df:
        gender_count=(df['Gender'].value_counts())

        print('\nUser Gender')
        print(gender_count.index[0],': ',gender_count[0],' counts')
        print(gender_count.index[1],': ',gender_count[1],' counts')

    if 'Gender' not in df:
        print('\nNo Gender data available.')

        #Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        max_birth_year=max(df['Birth Year'])
        min_birth_year=min(df['Birth Year'])
        common_birth_year=df['Birth Year'].mode()[0]
        common_birth_year_count=max(df['Birth Year'].value_counts())

        print('\nUser birth year')
        print('The earliest birth year of our users is',int(min_birth_year),'.' )
        print('The latest birth year of our users is',int(max_birth_year),'.' )
        print('The most common birth year of our users is',int(common_birth_year),'with a count of',common_birth_year_count,'.' )

    if 'Birth Year' not in df:
        print('\nNo Birth Year data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data if uswer wants to."""
    start_loc=0
    answer_yes  = ['yes', 'y']
    repeat_5_rows = input("\nEnter 'Yes' if you want to see 5 rows of the raw data.\n >>> ")
    while (repeat_5_rows.lower() in answer_yes):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        repeat_5_rows = input("\nEnter 'Yes' if you want to see another 5 rows of the raw data.\n >>> ")

def main():
    answer_yes  = ['yes', 'y']
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nEnter 'yes' for restart.\n >>> ")
        if restart.lower() not in answer_yes:
            print('\n')
            print('Good Bye!')
            print('-'*40)
            break

if __name__ == "__main__":
	main()
