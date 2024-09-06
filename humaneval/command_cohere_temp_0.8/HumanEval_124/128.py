Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules. The date string is considered valid if all the rules are satisfied:
```python
def valid_date(date):
    """
    Validates a date string and returns True if valid, False otherwise.

    Args:
        date (str): Date string in the format "mm-dd-yyyy"

    Returns:
        bool: True if the date string is valid, False otherwise
    """
    import re

    date = date.strip()  # Remove leading and trailing spaces
    date = date.replace('/', '-')  # Convert '/' to '-'
    if not re.match(r"^[0-9]{2}-[0-9]{2}-[0-9]{4}$", date):
        return False

    year, month, day = map(int, date.split('-'))

    if 1 <= month <= 12:
        if month == 2 and day != 29:
            return False
        if month == 4 or month == 6 or month == 9 or month == 11 and day not in range(1, 31):
            return False
        if month != 2 and day not in range(1, 32):
            return False
    else:
        return False

    return True
```

The provided Python script defines a function `valid_date` that takes a date string as input and returns `True` if the date is valid according to the given rules, and `False` otherwise. The function first cleans the input date string and checks if it matches the "mm-dd-yyyy" format. It then extracts the year, month, and day components and checks if the month is within the valid range of 1 to 12. If it is, the function further checks day validity based on the month; days are restricted to ranges like 1-31, 1-30, or 1-29 depending on the month. If the month is not within the valid range, the function returns `False`. 

Overall, this code provides a clear and effective approach to validating date strings against specific rules, making it a valuable tool for handling date-related data in various applications.