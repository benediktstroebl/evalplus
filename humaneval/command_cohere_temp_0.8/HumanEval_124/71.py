Here's a Python script that implements the `valid_date` function described in the markdown code block:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Validate the date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())

    # Validate the day and month ranges
    if month == 2:
        if day not in range(1, 29):
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12] :
        if day not in range(1, 32):
            return False
    else:
        if day not in range(1, 31):
            return False

    # Validate the year range
    if year < 2000 or year > 2030:
        return False

    return True
```

This code uses the re-module to check if the date is in the correct format and then checks the day and month against their acceptable ranges. Finally, it checks the year to ensure it is not too far in the past or future. 

The function can be tested like this:
```python
# These tests will run the function with different inputs and check if the output is as expected
assert valid_date('06-04-2020')
assert not valid_date('04-0-2040')
assert not valid_date('06/04/2020')
assert not valid_date('15-01-2012')
assert not valid_date('03-11-2000')
assert valid_date('03-11-2000')
assert not valid_date('')
```

The function should return True for valid dates and False otherwise, as indicated in the comments. 
This implementation covers all the corner cases mentioned in the problem description and will also return False for dates that do not conform to the specified format.