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
    if (mm < 1 or mm > 12) or (dd < 1 or dd > diary_days(mm)):
        return False
    
    # Year checks
    if yyyy < 1000 or yyyy > 2030: 
        return False
    
    return True

def diary_days(month):
    # Returns the number of days in a month for given year
    if (month == 2): 
        return 29  
    elif (month == 4 or month == 6 or month == 9 or month == 11): 
        return 30 
    else: 
        return 31

# Example usage
date = '06-04-2020'
if(valid_date(date)):
    print("Valid Date")
else:
    print("Invalid Date")
```

This script uses a regular expression to parse the date format and extract the month, day, and year. 

The function `diary_days()` has been added to provide a simple way to get the maximum days in a month for a given month. This function returns 31 for all months except month 2 (29 days), month 4, 6, 9, and 11 (30 days).

The script validates the date based on the rules mentioned in the problem statement and returns True if the date is valid and False otherwise.

The example usage at the end demonstrates the function's behavior.