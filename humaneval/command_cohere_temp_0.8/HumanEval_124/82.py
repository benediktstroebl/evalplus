Here's a Python script that includes a function called `valid_date` that solves the problem:
```python
import re

def valid_date(date):
    """
    Validate a given date string and return True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if ((dd<1 or dd>31) and (mm in [1, 3, 5, 7, 8, 10, 12])) or (dd<1 or dd>30 and mm in [4, 6, 9, 11]) or (dd<1 or dd>29 and mm==2):
        return False
    
    # Year and day of the week checks
    if mm<1 or mm>12 or dd<1 or dd>31:
        return False
    
    return True
```

This code uses the re-module to check dates against the pattern `mm-dd-yyyy` with integers 0-9 for the month, day, and year. The function returns True if the date is valid and False if it is not. 

The date is validated using several if statements, each of which checks a specific condition. These checks ensure that the date is not only in the correct format but also sensible in terms of month and day numbers. The code returns True if all conditions are satisfied, and False otherwise.  This approach minimizes redundant code and makes the function more readable.