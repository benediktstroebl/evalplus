Here's a Python script that defines a function called `valid_date` to validate a date string and return `True` if the date is valid and `False` otherwise, following the specified rules:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    
    if not date_parts:
        return False
    
    year, month, day = map(int, date_parts.groups())
    
    # Check day validity for different months
    max_day = {
        1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31,
        12: 31, 2: 29, 4: 30, 6: 30, 9: 30, 11: 30
    }
    
    if day < 1 or day > max_day[month]:
        return False
    
    # Check month validity
    max_month = 12
    min_month = 1
    
    if month < min_month or month > max_month:
        return False
    
    return True

# Test cases
assert valid_date("06-04-2020")
assert not valid_date("06/04/2020")
assert not valid_date("15-01-2012")
assert not valid_date("04-0-2040")
assert not valid_date("")
```

This code will accurately validate date strings based on the given rules and return `True` for valid dates and `False` for invalid ones.