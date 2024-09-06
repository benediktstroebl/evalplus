Here's a Python script that implements the `valid_date` function described in the markdown code block:
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
    
    # Check if the date is valid
    if 1 <= month <= 12:
        if (month == 2 and day >= 1 and day <= 29) or 
            (month != 2 and day >= 1 and day <= 31):
            return True
        else:
            return False
    else:
        return False

# Test cases
assert valid_date("06-04-2020")
assert not valid_date("06/04/2020")
assert not valid_date("15-01-2012")
assert not valid_date("04-0-2040")
assert not valid_date("")
```

This script uses a regular expression to match the date format and extract the year, month, and day from the input date string. It then checks whether the month is within the valid range (1 to 12) and whether the day is within the valid range for the specific month. It returns `True` if all conditions are met and `False` otherwise.

The code includes test cases to validate the function behavior. You can add more test cases to cover other edge cases as per the problem statement.