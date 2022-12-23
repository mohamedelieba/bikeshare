# Explore Bikeshare Data

Udacity Nanodegree project

## Overview

In this project, you will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Datasets

> Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)
> The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

## Program Flow:

the program starts with asking the user about the desriable city to load its data then if he/she would like to filter the data by day, month, both, or none of them.

the program will show only five records that matches the chosen filter, then prompt the user if he/she would like to see more records to show the next five records and so on.

then the program will ask the user wether or not he would like to see statistics about his chosen filters.

finally, the program will ask the user if he would like to restart and reset his/her chosen filters.

you can exit the program saying "no" in the last prompt or using keyboard interupt signal e.g. ctrl+c.

## Statistics Computed

1. Popular times of travel (i.e., occurs most often in the start time)
    * most common month
    * most common day of week
    * most common hour of day

2. Popular stations and trip
    * most common start station
    * most common end station
    * most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration
    * total travel time
    * average travel time

4. User info
    * counts of each user type
    * counts of each gender (only available for NYC and Chicago)
    * earliest, most recent, most common year of birth (only available for NYC and Chicago)
