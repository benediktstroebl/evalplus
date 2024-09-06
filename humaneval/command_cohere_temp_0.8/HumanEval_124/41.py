Here's a Python script that implements the `valid_date` function described in the prompt:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False

    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())
    
    # Check month and day validity
    if ((month <= 2 and day > 29) or 
        (month == 2 and day != 29) or
        (month > 2 and (month == 4 or month == 6 or month == 9 or month == 11) and day > 30) or
        (month > 2 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day > 31)):
        return False

    # Check year validity
    if year < 2000 or year > 2040: 
        return False

    return True
```

This code uses the `re` module to check if the date is in the correct format. It then uses a series of if statements to check whether the date provided passes any of the criteria, returning False if it does not. The date is considered valid if it does not meet any of the conditions for expiration.