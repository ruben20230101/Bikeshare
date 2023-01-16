import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("\nHello! Let\'s explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWould you like to know more about Chicago, New York City, or Washington?\n").lower()
        if city not in CITIES:
            print("\nPlease choose either Chicago, New York City, or Washington\n")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSpecify a month from January until June or \'all\' to disable month filter\n").lower()
        if month not in MONTHS:
            print("\nPlease specify a month from January until June or \'all\' to disable filter\n")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nSpecify a day of the week or \'all\' to disable day filter\n").lower()
        if day not in DAYS:
            print("\nPlease specify a day of the week or \'all\' to disable filter\n")
            continue
        else:
            break

    print("-"*69)
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

   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of the week'] = df['Start Time'].dt.day_name() # (R) Why one parentheses and other one not???
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day of the week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    month_mode = df['Month'].mode()[0]
    print("The most popular month to start is {}".format(calendar.month_name[month_mode]))

    # display the most common day of week
    day_mode = df['Day of the week'].mode()[0]
    print("The most popular day to start is", day_mode.capitalize())

    # display the most common start hour
    hour_mode = df['Hour'].mode()[0]
    print("The most popular hour to start is", hour_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # display most commonly used start station
    start_mode = df['Start Station'].mode()[0]
    print("The most popular start station is", start_mode)

    # display most commonly used end station
    end_mode = df['End Station'].mode()[0]
    print("The most popular end station is", end_mode)

    # display most frequent combination of start station and end station trip
    combination_mode = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print(combination_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The cumulative time of trips taken is {} minutes".format(int(total_travel)))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The average time of a bike trip is {} minutes".format(int(mean_travel / 60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\n")
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest  = int(df['Birth Year'].min())
        print("\nEarliest birh year: ", earliest)
        latest  = int(df['Birth Year'].max())
        print("Latest birth year: ", latest)
        average  = int(df['Birth Year'].mean())
        print("Most common birh year: ", average)

    print(f"This took %s seconds.\n" % (time.time() - start_time))
    print("-"*69)

def raw_data(df):
    i = 0
    while True:
        raw_data = input("Would you like to see five (more) lines of raw data? Enter yes or no.\n").lower()
        if raw_data.lower() != 'yes':
            print("\nThe end.")
            break
        else:
            print(df.iloc[i:i+5,:])
            i += 5
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        print("\nThis project was brought to you by Ruben Dekker with love.")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
