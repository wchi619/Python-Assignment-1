#!/usr/bin/env python3
"""
OPS435 Assignment 1 - Fall 2019
Program: a1_wchi3.py
Author: William Chi

The python code in this file (a1_wchi3.py) is original work written by William Chi. No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. I have not shared this python script with anyone or anything except for submission for grading. I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.
This program will return the date in YYYY/MM/DD after the given day (second argument) is passed. This program requires 2 arguments with an optional --step flag.
"""

# Import package
import sys

def usage():
    """Begin usage check. """

    if len(sys.argv) != 3 or len(sys.argv[1]) != 10 or sys.argv[2].lstrip("-").isdigit() == False:  #Argument parameter check
        print("Error: wrong date entered")
        exit()
    else:  #If error check pass, continue program and return date and days
        date = str(sys.argv[1])
        days = int(sys.argv[2])
        return date, days

def valid_date(date):
    """Validate the date the user inputs.
    This function will take a date in "YYYY/MM/DD" format, and return True if the given date is a valid date, otherwise return False plus an appropriate status message. This function will also call another function to double check that the days in month entered is correct.
    """

    days_in_mon(date)

    # Begin date validation
    if int(date[0:4]) not in range(1, 2050):
        print("Error: wrong year entered")
        exit()
    elif int(date[5:7]) not in range(1, 13):
        print("Error: wrong month entered")
        exit()
    elif int(date[8:10]) not in range(1, 32):
        print("Error: wrong day entered")
        exit()
    elif leap_year(date) == False and date[5:7] == '02' and int(date[8:10]) in range(29,32):  # If not leap year but date entered is Feb 29-31
        print("Error: Invalid day entered (not a leap year).")
        exit()
    elif leap_year(date) == True and date[5:7] == '02' and int(date[8:10]) not in range(1,30):  # If leap year, but date entered is Feb 30-31
        print("Error: Invalid day entered (01-29 only).")
        exit()
    else:
        return True

def days_in_mon(date):
    """Creates dictionary of the maximum number of days per month.
    This function will take a year in "YYYY" format and return a dictionary object which contains the total number of days in each month for the given year. The function will also call another function to check for leap year.
    """

    leap_year(date)

    days_per_month = {
       '1' : 31,
       '2' : 28,
       '3' : 31,
       '4' : 30,
       '5' : 31,
       '6' : 30,
       '7' : 31,
       '8' : 31,
       '9' : 30,
       '10' : 31,
       '11' : 30,
       '12' : 31,
    }

    if leap_year(date) == True:
        days_per_month['2'] = 29  # Change Feb to 29 if leap year
        return days_per_month
    else:
        return days_per_month

def leap_year(date):
    """Double check if the year entered is a leap year or not.
    This function will take a year in "YYYY" format and return True if the year is a leap year, otherwise return False.
    """

    year = int(date[0:4])  # Grab year

    # Leap year test will only return True on 2 conditions:
    # 1. The century year is divisible by 400, OR 
    # 2. The year is divisible by 4 AND IS NOT divisible by 100 (omit century years).

    if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        return True
    else:
        return False

def after(date, days):
    """Returns the final calculated value of the date.
    This function will take a date and a positive integer, add the integer as the amount of days to the date and return the final date. This function will also call on another function to retrieve a dictionary of the total number of days per each month (also accounting for leap years).
    """

    dictionary = days_in_mon(date)

    year, month, day = date.split('/')

    year = int(year)
    month = int(month)
    day = int(day)

    # Define variables for the final month & day.
    nmonth = month
    nday = day

    for i in range(days):
        # Resets day to 1 if it exceeds the total days in a month.
        if nday >= dictionary[str(month)]:
            month = month + 1
            nday = 1
            nmonth = nmonth + 1
        else:
            nday = nday + 1

        # Resets month to 1 if it exceeds the total months in a year.
        if nmonth > 12:
            nmonth = 1
            month = 1
            year = year + 1

    n = str(year) + "/" + str(nmonth).zfill(2) + "/" + str(nday).zfill(2)

    return n

def before(date, days):
    """Returns the final calculated value of the date.
    This function will take a date and a negative integer, subtract the date with the amount of days and return the final date. This function will also call on another function to retrieve a dictionary of the total number of days per each month (also accounting for leap years).
    """

    dictionary = days_in_mon(date)

    year, month, day = date.split('/')

    year = int(year)
    month = int(month)
    day = int(day)


    # Define variables for the final month & day.
    nmonth = month
    nday = day

    for i in range(days, 0):
        if nday <= 1:
            month = month - 1
            if month == 0:
                month = 1
            # Set the month to the highest value allowed in that month.
            nday = dictionary[str(month)]
            nmonth = nmonth - 1
        else:
            nday = nday - 1

        # Reset month to 12 if it is lower than the total months in a year.
        if nmonth < 1:
            nmonth = 12
            month = 12
            year = year - 1

    n = str(year) + "/" + str(nmonth).zfill(2) + "/" + str(nday).zfill(2)

    return n

def dbda(date, days):
    """Calls the correct function to calculate the date.
    This function will retrieve the validated date and days and depending on the value of the integer it will call 2 separate functions.
    """
    if int(sys.argv[2]) >= 0:
        return after(date, days)
    else:
        before(date, days)
        return before(date, days)

if __name__ == "__main__":

    # Executed first: figure out if --step option is present or not, and pop itif necessary.
    if sys.argv[1] == '--step':
        step = True
        sys.argv.pop(1)
        usage()
    else:
        step = False
        usage()

    # Argument initialization    
    date = str(sys.argv[1])
    days = int(sys.argv[2])

    valid_date(date)  # Begin date validation.

    # Call calculation function to print the final date.
    if step == True:
        if days > 0:  # Loop to print positive date step by step.
            for i in range(1, days+1):
                final_date = dbda(date, i)
                print(final_date)
        else:  # Loop to print negative date step by step (reverse order).
            for i in reversed(range(days, 0)):
                final_date = dbda(date, i)
                print(final_date)

    if step == False:  # Loop to print normally if no --step option inputted.
        final_date = dbda(date,days)
        print(final_date)
