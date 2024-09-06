Here's a Python script that includes a function called `valid_date` that solves the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date_parts = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date).groups()
    except AttributeError:
        return False
    day, month, year = map(int, date_parts)

    if 1 <= month <= 12:
        max_days = 31 if (month == 1 or month == 3 or month == 5 or
                            month == 7 or month == 8 or month == 10 or month == 12) else 30
        if day < 1 or day > max_days:
            return False
    else:
        return False

    if year < 2000 or year > 2030:
        return False

    return True
```

This code uses the `re` module to parse the date string using a regular expression. The function then checks the validity of the date components like day of the month, month, and year. The year is validated to be between 2000 and 2030. Finally, if all the conditions are met, the function returns `True` if the date is valid, otherwise `False`.