Here's a Python script that implements the `valid_date` function described in the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Month checks
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30) and (dd < 1 or dd > 29):
        return False

    # Year check
    if mm < 1 or mm > 12 or dd < 1 or dd > days_in_month(mm, yyyy):
        return False
    
    return True

def days_in_month(mm, yyyy):
    days_in_month_table = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month_table[mm-1]

# Example usage
date_strings = [
    '06-04-2020',
    '06/04/2020',
    '15-01-2012',
    '04-0-2040',
    '03-11-2000'
]

invalid_dates = [date for date in date_strings if not valid_date(date)]

print("Valid Dates:")
for date in date_strings:
    if valid_date(date):
        print(date)

print("\nInvalid Dates:")
for date in invalid_dates:
    print(date)
```

This script includes a function `valid_date` that takes a date string as input and returns `True` if the date is valid and `False` otherwise. The function follows the criteria you provided in the problem description.

The script also includes a helper function `days_in_month` that calculates the number of days in a given month. This is used to validate the year component of the date. 

The example usage at the end demonstrates how the `valid_date` function works with a list of date strings and filters out the valid and invalid dates accordingly.