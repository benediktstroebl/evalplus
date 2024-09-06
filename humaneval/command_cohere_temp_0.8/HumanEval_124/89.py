Here's a Python script that implements the `valid_date` function described in the markdown code block:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Check day validity
    if month == 2 and day != 29:
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day < 1 or day > 31:
        return False
    elif month in [4, 6, 9, 11] and day < 1 or day > 30:
        return False
    
    # Check month validity
    if month < 1 or month > 12:
        return False
    
    # Check year validity
    if year < 1000:
        return False
    
    return True
```

This code uses the `re` module to validate the date format and ensures that the day and month values are within the acceptable ranges. The function checks the date components in the order mentioned in the problem statement, and returns `True` if all conditions are met, and `False` otherwise. 

You can test this function with various valid and invalid date strings to ensure it behaves as expected. 
Please let me know if you have any dates you'd like to test!  It's important to make sure the function is 100% confident of its correctness.