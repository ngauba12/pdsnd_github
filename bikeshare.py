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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Please enter the city name: ').lower()
    
    while city not in ['chicago', 'new york city', 'washington' ]:
        city=input('This city name is invalid. Please enter another city : ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month= input('Please enter the a particular month or all to select all months: ').lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the day of the week or all to select all days: ').lower()
    
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
    
    df=pd.read_csv('{}.csv'.format(city.replace(' ','_')))
    
    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())
    
    # filter by month if applicable
    if month!='all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
       
        df = df.loc[df['month'] == month,:]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('Most common month is '+str(common_month))
    


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is '+str(common_day))


    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_str = df['start_hour'].mode()[0]
    print('Most common start hour is '+str(common_str))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_ss = df['Start Station'].mode()[0]
    print('Most common start station is '+str(common_ss))


    # TO DO: display most commonly used end station
    common_es = df['End Station'].mode()[0]
    print('Most common end station is '+str(common_es))


    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " -> " + df['End Station']
    common_r=df['routes'].mode()[0]
    print('Most common start and end station combination is '+str(common_r))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['duration']= df['End Time'] - df['Start Time']

    # TO DO: display total travel time
    print('Total Travel time is: {}'.format(str(df['duration'].sum())))


    # TO DO: display mean travel time
    print('Mean travel time is: {}'.format(str(df['duration'].mean())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here are the counts of various user types: {}".format(str(df['User Type'].value_counts())))
    
    # TO DO: Display counts of gender
    if city != 'washington':
        print('Here are the counts of gender: {}'.format(str(df['Gender'].value_counts())))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is: {}'.format(str(int(df['Birth Year'].min()))))
        
        print('Most recent year of birth is: {}'.format(str(int(df['Birth Year'].max()))))
       
        print('Most common year of birth is: {}'.format(str(int(df['Birth Year'].mode()[0]))))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """
    
    start_loc = 0
    end_loc = 5
    
    display_active = input("Do you want to see the raw data?: ").lower()
    
    if display_active == 'yes':
        while end_loc <= df.shape[0]-1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc+=5
            end_loc+=5
        
            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break
            
        
        
                
    
  



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
