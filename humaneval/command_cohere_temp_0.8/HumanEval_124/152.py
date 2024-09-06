Here's a Python script that defines a function to validate a date string according to the given problem statement:
```python
import re

def valid_date(date):
    """
    Validate a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False

    # Check if date string matches the pattern mm-dd-yyyy
    match = re.match(r"^(\d{2})[-/](\d{2})[-/](\d{4})$", date)
    if not match:
        return False

    mm, dd, yyyy = map(int, match.groups())

    # Check if the day and month combination is valid
    if (dd > 31 and (mm == 2 or mm in [4, 6, 9, 11])) or \
            (dd > 30 and mm in [1, 3, 5, 7, 8, 10, 12]) or \
            dd > 29:
        return False

    # Check if the month is in the valid range
    if mm < 1 or mm > 12:
        return False

    return True
```

This code uses the re-module to validate the date format and checks the validity of the number of days and months. 

You can use this function to validate date strings and return 'True' if the date is valid and 'False' otherwise. 
Feel free to ask any questions or provide additional feedback!