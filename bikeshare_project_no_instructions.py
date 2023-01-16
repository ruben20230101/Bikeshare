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

    print("\nHello! Let\'s explore some US bikeshare data!")
    while True:
        city = input("\nWould you like to know more about Chicago, New York City, or Washington?\n").lower()
        if city not in CITIES:
            print("\nPlease choose either Chicago, New York City, or Washington\n")
            continue
        else:
            break
    while True:
        month = input("\nSpecify a month from January until June or \'all\' to disable month filter\n").lower()
        if month not in MONTHS:
            print("\nPlease specify a month from January until June or \'all\' to disable filter\n")
            continue
        else:
            break
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

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month
    df['Day of the week'] = df['Start Time'].dt.day_name() # (R) Why one parentheses and other one not???
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day of the week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    month_mode = df['Month'].mode()[0]
    print("The most popular month to start is {}".format(calendar.month_name[month_mode]))

    day_mode = df['Day of the week'].mode()[0]
    print("The most popular day to start is", day_mode.capitalize())

    hour_mode = df['Hour'].mode()[0]
    print("The most popular hour to start is", hour_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def station_stats(df):

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    start_mode = df['Start Station'].mode()[0]
    print("The most popular start station is", start_mode)

    end_mode = df['End Station'].mode()[0]
    print("The most popular end station is", end_mode)

    combination_mode = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
    print(combination_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    total_travel = df['Trip Duration'].sum()
    print("The cumulative time of trips taken is {} minutes".format(int(total_travel)))

    mean_travel = df['Trip Duration'].mean()
    print("The average time of a bike trip is {} minutes".format(int(mean_travel / 60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-"*69)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)
    print("\n")
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

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

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
	main()
