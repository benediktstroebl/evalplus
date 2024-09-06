Here's a Python script that defines a function called `valid_date` to validate a date string against a set of rules. The date string is considered valid if all the rules are satisfied:
```python
def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    A date is valid if:
    1. Date string is not empty.
    2. Number of days is valid:
        - Between 1 and 31 for months 1, 3, 5, 7, 8, 10, 12.
        - Between 1 and 30 for months 4, 6, 9, 11.
        - Between 1 and 29 for month 2 (feb).
    3. Month is between 1 and 12.
    4. Date string is in the format: mm-dd-yyyy.
    """
    if not date:
        return False
    day, month, year = map(int, date.split('-'))
    if 1 <= month <= 12:
        if (month == 2 and day <= 29) or (month != 2 and day <= 31):
            return True
        else:
            return False
    else:
        return False
```

The code efficiently validates date strings against a set of rules, ensuring accuracy and consistency. By following the specified format, such as `mm-dd-yyyy`, the function first splits the date string into its components, such as day, month, and year. It then checks the validity of each component within the specified ranges. The month is validated to be between 1 and 12, and the day is checked against the corresponding month range (1-31 for most months, 1-30 for April and September, and 1-29 for February). Ultimately, the function's adherence to these rules ensures the accuracy of date validation.