Here's a Python script that implements the `valid_date` function described in the prompt:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.sub(r'[^0-9]', '', date).split('-'))
    
    # Check if the date is in the correct format (mm-dd-yyyy)
    if not re.match(r'^(\d{1,2})-(\d{1,2})-(\d{4})$', date):
        return False
    
    # Check if the day is valid for the specific month
    days_valid_for_month = [31, 30, 31, 30, 31, 30, 31, 30, 31]
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        if 1 <= dd <= days_valid_for_month[mm - 1]:
            return True
        else:
            return False
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if 1 <= dd <= days_valid_for_month[mm - 1]:
            return True
        else:
            return False
    elif mm == 2:
        if 1 <= dd <= 29:  # Allow for leap years
            return True
        else:
            return False
    
    # Check if the month is valid (1-12)
    if 1 <= mm <= 12:
        return True
    else:
        return False

# Test cases
print(valid_date('06-04-2020'))  # Should print True
print(valid_date('03-11-2000'))  # Should print True
print(valid_date('15-01-2012'))  # Should print False
print(valid_date('04-0-2040'))  # Should print False
print(valid_date('06/04/2020'))  # Should print False
print(valid_date(''))  # Should print False
```

This script extracts the year, month, and day from the date string using a regular expression, then checks the validity of the day and month using the predefined `days_valid_for_month` list, and finally checks if the month is within the valid range (1-12). The function returns `True` if all conditions are met and `False` otherwise.