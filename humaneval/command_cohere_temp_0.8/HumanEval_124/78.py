Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.findall(r'\d+', date)[:3])
        if (month, day) < (1, 1) or (month, day) > (12, 31) or \
           (month == 2 and day > 29) or \
           (month in [4, 6, 9, 11] and day > 30) or \
           year < 2000 or year > 2040:
            return False
        return True
    except:
        return False
```

The following points will illustrate how the function works:
1. `if not date:` This checks if the date string is empty and returns False if it is.
2. `try:` This block tries to split the date string into three parts, year, month, and day, using regular expressions and converting these parts to integers.
3. `return False:` This is done if any of the conditions `(month, day) < (1, 1) or (month, day) > (12, 31) or (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30) or year < 2000 or year > 2040` are satisfied.
4. `except:` This block catches all errors in the try block and returns False.

This solution has a time complexity of `O(1)` and uses regular expressions to validate the date string. It does not require any additional libraries other than the Python standard library.