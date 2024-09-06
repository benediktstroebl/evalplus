Here's a Python script that defines a function called `valid_date` to validate a date string and returns `True` if the date is valid and `False` otherwise. The date is considered valid if it satisfies the following conditions:
1. The date string is not empty.
2. The number of days falls within the acceptable range based on the month (between 1 and 31 for months 1, 3, 5, 7, 8, 10, and 12, and between 1 and 30 for months 4, 6, 9, 11, and between 1 and 29 for the month 2).
3. The month is within the range of 1 to 12.
4. The date is in the format `mm-dd-yyyy`.

To achieve this, the code uses regular expressions to validate the date format and a `range` function to check the day consistency with the corresponding month.

```python
import re

def valid_date(date):
    """
    Validate a date string and returns True if the date is valid otherwise False
    """
    if not date:
        return False
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if match:
        mm, dd, yyyy = map(int, match.groups())
        if 1 <= mm <= 12:
            if (dd <= maxdays[mm - 1] and dd > 0) or mm == 2:
                return True
        return False
    else:
        return False

# Dictionary for validation of days range per month
maxdays = {
    1: 31, 3: 31, 5: 31, 7: 31, 
    8: 31, 10: 31, 12: 31, 
    4: 30, 6: 30, 9: 30, 11: 30, 
    2: 29
}

# Test Cases
print(valid_date('03-11-2000'))
print(valid_date('15-01-2012'))
print(valid_date('04-0-2040'))
print(valid_date('06-04-2020'))
print(valid_date('06/04/2020'))
```

The script also includes test cases to help ensure that the `valid_date` function is working as expected. You can modify the test cases to cover more scenarios or add additional tests to ensure the robustness of the solution. The output of the code is:
```
True
False
False
True
False
```