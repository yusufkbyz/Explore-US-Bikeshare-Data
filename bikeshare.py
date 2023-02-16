import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            cities = ['chicago', 'washington', 'new york city']
            city = input('\nWhich city would you like to get information on (Chicago, New York City or Washington)?\n').lower()
            if city not in cities:
                print('\nPlease pick between Chicago, New York City or Washington.')
            else:
                break   
        except ValueError or AttributeError:
            print('\nPlease pick between Chicago, New York City or Washington. No numbers.')

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    while True:
        try:
            month = input('\nWhich month would you like to get data on (all, january, february, ...)?\n').lower()
            if month in months or month == 'all': # evaluating the input
                break
            else:
                print('\nPlease enter a valid month (or type \'all\').')
        except ValueError or AttributeError: # handling possible errors
            print('\nPlease enter a valid month (or type \'all\').')


    # get user input for day of month
        # defining preliminary variables
    max_months = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
        }

        # main loop to get an input for the day
    while True:
        try:
            day = input('\nWhich day of the month would you like to get information on (1,2,...,all)?\n').lower()
            day = int(day)
            if month == 'all': # evaluating the input
                if day > 31:
                    print('\nThe value entered is too high! Please enter a number between 1-31.')
                else:
                    break
            else:
                if int(max_months[month]) < day:
                    print('\nThe value entered is too high! Please enter a number between 1-{}'.format(int(max_months[month])))
                elif day < 1:
                    print('\nThe value entered is too low! Please enter a number between 1-{}'.format(int(max_months[month])))
                else:
                    break
        except ValueError or AttributeError: # handling possible errors
            if day == 'all':
                break
            else:
                print('\nPlease enter a valid day of the month (1,2,...,all).')

    print('-'*40)
    return city, month, day


def load_data(city, month1, day1):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # preliminary variable
    months = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12
        }

    # reading and processing the csv file
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month # creating new columns for easier processing
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # conditional statements to process output
    if day1 == 'all' and month1 == 'all':
        None
    elif day1 == 'all' and month1 != 'all':
        df = df.loc[df.month == int(months[month1])]
    elif month1 == 'all' and day1 != 'all':
        df = df.loc[df.day == int(day1)]
    else:
        df = df.loc[df.day == int(day1)]
        df = df.loc[df.month == int(months[month1])]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # preliminary code
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12:'December'
    }

    # display the most common month
    popular_month = df['month'].mode()[0]
    pmc = df['month'].value_counts()[popular_month]
    print('The most common month is {} ({} entries).'.format(months[popular_month], pmc))


    # the most common day of week
    popular_day = df['day'].mode()[0]
    pdct = df['day'].value_counts()[popular_day]

    # adding an ending to each day
    if popular_day % 10 == 1:
        day_str = 'st'
    elif popular_day % 10 == 2:
        day_str = 'nd'
    elif popular_day % 10 == 3:
        day_str = 'rd'
    else:
        day_str = 'th'

    # displaying the most common day of the week
    print('The most common day is the {}{} ({} entries).'.format(popular_day, day_str, pdct))


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    phct = df['hour'].value_counts()[popular_hour]
    print('Hour {} is the most common start hour ({} entries).'.format(popular_hour, phct))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    pssct = df['Start Station'].value_counts()[popular_sstation]
    print("The most commonly used Start Station is: {} ({} entries)".format(popular_sstation, pssct))

    # display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    pesct = df['End Station'].value_counts()[popular_estation]
    print("The most commonly used End Station is: {} ({} entries)".format(popular_estation, pesct))

    # display most frequent combination of start station and end station trip
    popular_combo = (df['Start Station'] + ' + ' + df['End Station']).mode()[0]
    pcmct = (df['Start Station'] + ' + ' + df['End Station']).value_counts()[popular_combo]
    print("The most frequent combination of start station and end station trip: {} ({} entries)".format(popular_combo, pcmct))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_time = round((df['Trip Duration'].sum())/60,2)
    print('The total travel time is: {} minutes.'.format(sum_time))

    # display mean travel time
    mean_time = round((df['Trip Duration'].mean())/60,2)
    print('The mean travel time is: {} minutes.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cnt_subss = df['User Type'].value_counts()['Subscriber']
    cnt_subsc = df['User Type'].value_counts()['Customer']
    print('Subscriber count: {} | Customer count: {}'.format(cnt_subss, cnt_subsc))

    # Display counts of gender
    try:
        cnt_gendm = df['Gender'].value_counts()['Male']
        cnt_gendf = df['Gender'].value_counts()['Female']
        print('Male count: {} | Female count: {}'.format(cnt_gendm, cnt_gendf))
    except KeyError: # handling possible missing data
        None

    # Display earliest, most recent, and most common year of birth
    try:
        cnt_earl = int(df['Birth Year'].min())
        cnt_late = int(df['Birth Year'].max())
        cnt_com = int(df['Birth Year'].mode()[0])
        cnt_comcnt = df['Birth Year'].value_counts()[cnt_com]
        print('Youngest patreon\'s year of birth: {}'.format(cnt_earl))
        print('Most mature patreon\'s year of birth: {}'.format(cnt_late))
        print('Most common year of birth: {} ({} entries)'.format(cnt_com, cnt_comcnt))
    except KeyError: # handling possible missing data
        None

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays raw data 5 rows at a time based on the user's input."""

    # dropping the appended columns
    df.drop(['month', 'day', 'hour'], inplace=True, axis=1)

    # main while loop for the whole process
    while True:
        # preliminary variables that will be used within the function
        n = -5
        m = 0
        try:
            # getting user input
            ques = input('\nWould you like to view the raw data (yes or no)?\n').lower()
            if ques == 'yes' or ques == 'no':
                # nested while loop no.2 for printing raw data
                while True:
                    n += 5
                    m += 5
                    print(df.iloc[n:m])
                    # nested while loop no.3 for validating user input
                    while True:
                        try: 
                            more = input('\nWould you like to view following five rows of raw data?\n').lower()
                            if more == 'no' or more == 'yes':
                                break
                            else:
                                print('\nPlease type \'yes\' or \'no\' only.')
                        except ValueError or AttributeError:
                            print('\nPlease type \'yes\' or \'no\' only.')
                    if more == 'no':
                        break
                    elif (m + 5) >= len(df): # predicts whether next iter is the last
                        print(df.tail())
                        print('\nThis is where the raw data ends.')
                        break
                    else:
                        None
                break
            else:
                print('\nPlease type \'yes\' or \'no\' only.')
        except ValueError or AttributeError:
            print('\nPlease type \'yes\' or \'no\' only.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()