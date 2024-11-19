#!/usr/bin/env python3

"""
OPS435 Assignment 1
Program: assignment1.py
Author: "rrakshit"
The python code in this file is original work written by the author.
"""

import sys

def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in a given month."""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 31

def next_day(year, month, day):
    """Return the next day as (year, month, day)."""
    if day < days_in_month(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def valid_date(date_str):
    """Validate if a given date string is in YYYY-MM-DD format and is valid."""
    try:
        year, month, day = map(int, date_str.split('-'))
        return 1 <= month <= 12 and 1 <= day <= days_in_month(year, month)
    except ValueError:
        return False

def count_weekends(start_date, end_date):
    """Count the number of weekends (Saturdays and Sundays) between two dates."""
    weekends = 0
    year, month, day = map(int, start_date.split('-'))
    end_year, end_month, end_day = map(int, end_date.split('-'))

    while (year, month, day) <= (end_year, end_month, end_day):
        day_of_week = (year + year // 4 - year // 100 + year // 400 +
                       sum(days_in_month(year, m) for m in range(1, month)) + day) % 7
        if day_of_week in {6, 0}:  # Saturday (6) or Sunday (0)
            weekends += 1
        year, month, day = next_day(year, month, day)

    return weekends

def usage():
    """Print usage instructions."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    exit(1)

def main():
    if len(sys.argv) != 3:
        usage()

    start_date, end_date = sys.argv[1], sys.argv[2]
    if not (valid_date(start_date) and valid_date(end_date)):
        usage()

    # Ensure start_date is earlier
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    weekends = count_weekends(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {weekends} weekend days.")

if __name__ == "__main__":
    main()
