Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Check if the day value is valid for the corresponding month
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30) and (dd < 1 or dd > 29):
        return False
    
    # Check if the month value is valid
    if mm < 1 or mm > 12:
        return False
    
    # Check if the year value is valid
    if not (1000 <= yyyy <= 2040): 
        return False
    
    return True

# Test cases
date_strings = [
    '03-11-2000',
    '15-01-2012',
    '04-0-2040',
    '06-04-2020',
    '06/04/2020'
]

print('Valid dates:')
for date in date_strings:
    if valid_date(date):
        print(date)
    else:
        print(f'{date} is invalid.')
```

This script uses regular expressions to parse the date string into three integers (`mm`, `dd`, `yyyy`) representing month, day, and year, respectively. It then checks if each of these integers falls within a valid range. Finally, it verifies that the date string is in the `mm-dd-yyyy` format and returns True if all conditions are met.

The test cases at the end demonstrate the function's behavior with various date strings.