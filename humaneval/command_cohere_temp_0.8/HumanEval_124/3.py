Here's a Python script that implements the `valid_date` function described in the prompt:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Check format
    if not re.match(r"^(\d\d?)-[\d\d]-[\d\d\d\d]$", date):
        return False
    
    # Extract day, month, and year
    day, month, year = map(int, date.split('-')[0:3])
    
    # Check month and day validity
    if month < 1 or month > 12:
        return False
    elif month == 2 and day > 29:
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False

    return True
```

This code uses the `re` module to check that the date string matches the expected format. It then splits the date string into day, month, and year, and checks that the day and month are within the valid ranges. Finally, it returns `True` if all the conditions are met, and `False` otherwise. 

Note that this code assumes that the date string follows the format `mm-dd-yyyy`, where `mm` represents the month, `dd` represents the day, and `yyyy` represents the four-digit year. 

You can test this function by calling it with different date strings to see if it returns the expected results based on the problem statement.