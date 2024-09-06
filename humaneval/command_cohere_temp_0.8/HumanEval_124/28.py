Here's a Python script that implements the `valid_date` function described in the markdown code block:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False

    # Check if date string is in the correct format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-[\d]{2}-[\d]{4}$", date)
    if not match:
        return False

    year, month, day = map(int, match.groups())
    
    # Checks for each month's day count
    days_per_month = [
        31,  # Jan, Mar, May, Jul, Aug, Oct, Dec
        30,  # Apr, Jun, Sep, Nov
        29  # Feb
    ]

    if month == 2:
        if day not in [1, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
            return False
    else:
        if day < 1 or day > days_per_month[month - 1]:
            return False

    # Check for valid range of months
    if month < 1 or month > 12:
        return False

    return True

# Example usage
date_strings = [
    "03-11-2000",
    "15-01-2012",
    "04-0-2040",
    "06-04-2020",
    "06/04/2020"
]

print(date_strings)
print(list(map(valid_date, date_strings)))
```
This script will return a list of boolean values indicating whether each date string is valid according to the given criteria.