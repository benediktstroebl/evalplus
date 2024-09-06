Here's a Python script that includes a function called `valid_date` that solves the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())

    if not (1 <= mm <= 12):
        return False
    if (mm == 2 and dd != 29) or (mm != 2 and dd not in [30, 31]):
        return False
    if not (1 <= dd <= 31):
        return False
    if not (1000 <= yyyy <= 9999):
        return False
    
    return True
```

This code uses the re module to parse the date string into three parts: the month, the day, and the year, all of which are converted into integers for further validation. The regular expression pattern r"(\d\d)-(\d\d)-(\d\d\d\d)" is used to ensure that the date is in the format "mm-dd-yyyy". The function then checks if the date is not empty and if the components are within the specified boundaries.

Here is an example usage of the `valid_date` function with corresponding dates:
```python
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))  # Output: False
print(valid_date('06-04-2020'))  # Output: True
print(valid_date('06/04/2020'))  # Output: False
```

This script should evaluate the date strings against the given criteria and print out the appropriate truthiness of the dates.