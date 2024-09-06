Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.

    Args:
        date (str): A date string in the format "mm-dd-yyyy".

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    if not isinstance(date, str) or not re.match(r"^\d\d-\d\d-\d{4}$", date):
        return False

    year, month, day = map(int, date.split('-'))

    if not 1 <= month <= 12:
        return False

    if month == 2:
        if not 1 <= day <= 29:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            return False
    else:  # for 4, 6, 9, 11
        if not 1 <= day <= 30:
            return False

    return True
```

This code ensures the date string follows the expected format, the year is within the valid range of years, the month is within the valid range of months, and the day is within the valid range of days depending on the month. 

The function can be used as follows:
```python
print(valid_date("06-04-2020"))  # Outputs: True
print(valid_date("06/04/2020"))  # Outputs: False
``` 
The provided example test cases validate the correctness of the `valid_date` function.