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
    date_parts = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)

    if not date_parts:
        return False

    year, month, day = date_parts.groups()

    # Check if the date is valid
    if not (1 <= int(month) <= 12 and
                1 <= int(day) <= np_days[month - 1] and
                2000 <= int(year) <= 2030):
        return False

    return True

# Dictionary for the number of days in a month
np_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
```

This script uses regular expressions to match the date format and extract the year, month, and day components. It then checks these components against the predefined rules to determine if the date is valid or not.

The `valid_date` function will return `True` for valid dates and `False` for invalid ones, based on the specified rules.

Note that this code uses a dictionary `np_days` to store the number of days for each month, assuming a range from 2000 to 2030. You may need to adjust these values depending on the specific range of valid years in your use case.