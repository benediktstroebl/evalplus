Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', date).groups())
        if (month, day) < (1, 1) or (month, day) > (12, 31) or \
           (month == 2 and day > 29) or \
           (month in [4, 6, 9, 11] and day > 30) or \
           year < 2000 or year > 2040:
            return False
    except AttributeError:  # Raised if re.match fails (e.g., wrong date format)
        return False
    return True
```

This code utilizes a regular expression to validate the date format and parses it into 3 integers representing day, month, and year. These values are checked against predefined rules to validate dates' range whereas the month range validation incorporates an exception for February. Finally, the date is validated by checking that its year is within the range of 2000-2040. The function will return False if any of the aforementioned rules are violated, whereas it will return True if all the rules are satisfied.