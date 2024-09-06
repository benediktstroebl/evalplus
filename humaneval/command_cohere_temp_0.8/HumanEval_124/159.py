Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules:
```python
import re

def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    """
    if not date:
        return False

    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())

    # Check day validity
    if 1 <= month <= 12:
        if 1 < day < days_in_month(month):
            return True
        else:
            return False
    else:
        return False

    return True

def days_in_month(month):
    # Number of days in each month
    months_days = [
        31,   # January
        29,   # February (leap year)
        31,   # March
        30,   # April
        31,   # May
        30,   # June
        31,   # July
        31,   # August
        30,   # September
        31,   # October
        30,   # November
        31,   # December
    ]
    if 1 <= month <= 12:
        return months_days[month - 1]
    else:
        return 0

```

This script defines a function `valid_date` that takes a date as input in the format "mm-dd-yyyy" and returns `True` if the date is valid and `False` otherwise. The function checks that the date is not empty, has the correct format, and satisfies rules about the range of valid days and months. 

It utilizes the `re` module to check the format of the date string and the `days_in_month` function to determine if the day is valid for the specified month. 

Let's break down the code:
1. **Importing the `re` module**: This module is used for regular expression operations.
2. **Function `valid_date(date)`**: This function takes a date string as its argument and returns `True` if the date is valid and `False` otherwise.
3. **Checking for Empty Date**: The function first checks if the date string is empty, and if so, it returns `False` immediately.
4. **Valid Date Format**: The function uses a regular expression to check if the date string has the correct format ("mm-dd-yyyy"). If it doesn't match this pattern, it returns `False`.
5. **Converting Date Components to Numbers**: If the date string has the correct format, the function uses the `map` function to convert the three parts (day, month, and year) to integers.
6. **Day Validation**: The function then checks if the day is valid for the specified month. This is done by checking if the month is within the range of 1 to 12 and calling the `days_in_month` function to get the number of days for the specified month. If the day is within the valid range for the specific month, it returns `True`. Otherwise, it returns `False`.
7. **Return Validation Status**: After all checks, the function returns `True` if the date is valid and `False` otherwise.

This solution is efficient and doesn't have any obvious bottlenecks. The regular expression is used for validation, which can be slower than other checks but is generally efficient for this type of string-matching task.

The `days_in_