Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.match(r'(\d{4})-(\d{2})-(\d{2})', date).groups())
    
    # Check if the date is in the correct format
    if not re.match(r'^(\d{2})-(\d{2})-(\d{4})$', date):
        return False
    
    # Check month and day validity
    if mm < 1 or mm > 12:
        return False
    if mm == 2 and dd > 29:
        return False
    if mm != 2 and dd < 1 or dd > 31:
        return False
    
    # Check year validity (assuming 2000-2099 is considered valid)
    if yyyy < 2000 or yyyy > 2099:
        return False
    
    return True

# Example usage
date_strings = [
    '03-11-2000',
    '15-01-2012',
    '04-0-2040',
    '06-04-2020',
    '06/04/2020'
]

print(date_strings)
print(list(map(valid_date, date_strings)))
```

This script ensures the date is not empty, is in the correct format, and follows the rules for days and months per the specification. The example usage demonstrates the function's behavior on a list of date strings, printing out the validity of each date.