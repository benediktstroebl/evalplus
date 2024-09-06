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
    
    mm, dd, yyyy = map(int, match.groups())
    
    # Check day validity
    if mm == 2:
        if dd < 1 or dd > 29:
            return False
    elif mm in [1, 3, 5, 7, 8, 10, 12] :
        if dd < 1 or dd > 31:
            return False
    elif mm in [4, 6, 9, 11] : 
        if dd < 1 or dd > 30:
            return False
    
    # Check month validity
    if mm < 1 or mm > 12:
        return False
    
    # If all checks passed, the date is valid
    return True

# Example usage:
date1 = '03-11-2000'
date2 = '15-01-2012'
date3 = '04-0-2040'
date4 = '06-04-2020'
date5 = '06/04/2020'

print(valid_date(date1))  # Output: True
print(valid_date(date2))  # Output: False
print(valid_date(date3))  # Output: False
print(valid_date(date4))  # Output: True
print(valid_date(date5))  # Output: False
```

This script uses regular expressions to validate the date format and then checks the validity of the date components (day and month) based on the given rules. The function will return `True` if the date is valid and `False` otherwise.

The example usage block demonstrates how the `valid_date` function works on different date inputs.