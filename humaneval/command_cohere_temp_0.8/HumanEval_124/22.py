Here's a Python script that includes a function called `valid_date` that solves the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/\s](\d{1,2})[-/\s](\d{4})', date))
    
    # Checks for constraints on month and day
    if (
        (dd<1 or dd>31) if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12) else
        (dd<1 or dd>30) if (mm==4 or mm==6 or mm==9 or mm==11) else
        (dd<1 or dd>29) if mm==2 else True
    ):
        return False
    
    # Check for constraint on year
    if yyyy<1000 or yyyy>9999:
        return False
    
    # Check for valid date format
    if not re.match(r'^(\d{2})[-/\s](\d{1,2})[-/\s](\d{4})$', date):
        return False
    
    return True
```

This code will validate a date string in the format `mm-dd-yyyy`, where:
- `mm` represents the two-digit month number.
- `dd` represents the two-digit day number.
- `yyyy` represents the four-digit year number.

The function checks the date against a set of constraints:
1. The date string must not be empty.
2. The day value must be between 1 and 31 for months 1, 3, 5, 7, 8, 10, and 12, between 1 and 30 for months 4, 6, 9, and 11, and between 1 and 29 for the month 2.
3. The month value must be between 1 and 12.
4. The date string must conform to the `mm-dd-yyyy` format.

The function will return `True` if all constraints are met and the date is valid. If any constraint is not met, the function will return `False`. 

This implementation allows you to quickly validate a date string within the specified format and constraints, which is ideal for scenarios where you need to check dates within a range or handle date-related data.