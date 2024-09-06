Here's a Python script that implements the `valid_date` function, with corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d{2}-\d{2}-\d{4}', date))
    
    # Validate day and month
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30):
        return False
    if (mm < 1 or mm > 12):
        return False
    
    # Validate year
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    return True

# Tests
test_dates = [
    '03-11-2000',
    '06-04-2020',
    '15-01-2012',
    '04-0-2040',
    '06/04/2020',
    '',
    '05-02-2021',
    '02-29-2021',
    '01-01-2001',
    '13-01-2012',
    '02-02-2021',
]

test_results = [
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    False,
    True,
    True,
    False,
]

for i in range(len(test_dates)):
    assert valid_date(test_dates[i]) == test_results[i]
```

This script includes a function `valid_date` that takes a date as input and returns `True` if the date is valid and `False` otherwise. The function checks that the date is not empty, has the correct format, and satisfies rules about the range of days and months. The function also checks that the year is within the range of 1000 to 3000. The tests are provided in the code and the results are compared against the expected output.  You can add more tests to test other edge cases if needed.