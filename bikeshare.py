import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    #get user input for city (chicago, new york city, washington)
    city = str(input("Enter a City")).lower()
    while( city.lower() !="chicago" and city.lower()!= "new york city" and city.lower()!= "washington"):
        city = str(input("Kindly, choose one of these cites:chicago, new york city, washington")).lower()
        
    
    
    #get user input for month (all, january, february, ... , june)
    month = str(input("Enter a month or all")).lower()
    while( month.lower() !="all" and month.lower()!= "january" and month.lower()!= "june" and month.lower()!= "february" and month.lower()!= "march" and month.lower()!= "april" and month.lower()!= "may"):
        month = str(input("Kindly, all, january, february, ... , june")).lower()
        
        
        #get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Enter a day or all")).lower()
    while( day.lower() !="all" and day.lower()!="sunday" and day.lower()!="monday" and day.lower()!="friday" and day.lower()!= "wednesday" and day.lower()!= "thursday" and day.lower()!= "saturday" and day.lower()!= "tuesday"):
        day = str(input("Kindly, all, tuesday, wednesday,... Monday ")).lower()
        

    print('-'*40)
    return city, month, day


#based on the user input, load_data will return the data to then be used for generating statistics
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city]) 

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month  ######test this one
    df['day_of_week'] = df['Start Time'].dt.weekday_name ####try .day


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  ############Test this

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #displaying the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    print('Most Frequent Month is {}'.format(df['month'].value_counts(). idxmax()))


    #displaying the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print('Most Frequent Day is {}'.format(df['day_of_week'].value_counts(). idxmax()))

    #displaying the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    print('Most Frequent Start Hour is {}'.format(df['hour'].value_counts(). idxmax()))
    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #displaying most commonly used start station
    print("Most commonly used start station is {}".format(df['Start Station'].max()))


    #displaying most commonly used end station
    print("Most commonly used end station is {}".format(df['End Station'].max()))


    #displaying most frequent combination of start station and end station trip
    print("Most Frequent Combination of Start Station and End Station Trip is {}".format(df.groupby(['Start Station', 'End Station']).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #displaying total travel time
    print("Displaying Total Travel time is {}".format(df['Trip Duration'].sum()))

    #displaying mean travel time
    print("Displaying Mean Travel time is {}".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    #user_types = df['User Type'].value_counts()
    print("Displaying counts of user types {}".format(df['User Type'].value_counts()))

    try:
        #Display counts of gender
        print("Displaying counts of user's gender {}".format(df['Gender'].value_counts()))
    except:
        print("The Dataset does not inculde infomration about the users gender")

    try:
        #Display earliest, most recent, and most common year of birth
        print("Most Recent Birth Year is {}".format(df['Birth Year'].max())) #this one for the most recent
        print("The Earliest Birth Year is {} ".format(df['Birth Year'].min())) #this one for the earliest
        print("The Most Common Birth Year is {}".format(df['Birth Year'].mode())) #this one for the most commen
    
    except:
        print("The Dataset does not inculde infomration about the users birth year")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display = input("DO you want to display users data? YES or NO").lower()
        while(display != 'yes' and display != 'no'):
            print("Kindly, choose yes or no")
            display = input("DO you want to display users data? YES or NO").lower()
        i = 0
        while (display == "yes"):
            print(df.iloc[i:i+5])
            i=i+5
            display = input("DO you want to display users data? YES or NO").lower()
            while(display != 'yes' and display != 'no'):
                print("Kindly, type yes or no")
                display = input("DO you want to display users data? YES or NO").lower()
                
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
