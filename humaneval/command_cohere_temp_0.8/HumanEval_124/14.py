Here's a Python script that implements the `valid_date` function described in the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or  (
            (mm == 2 and dd > 29) or 
            (mm in [1, 3, 5, 7, 8, 10, 12] and dd > 31) or 
            (mm in [4, 6, 9, 11] and dd > 30)
    ):
        return False
    
    # Day checks
    if dd < 1 or dd > 31:
        return False
    
    return True
```

This code uses regular expressions to split the date string into three parts: month, day, and year, and then checks the validity of each part. The function returns `True` if all checks pass and `False` otherwise.

You can test this function by calling it with different date strings. Here's an example:
```python
print(valid_date("06-04-2020"))  # Should print: True
print(valid_date("03-00-2000"))  # Should print: False
print(valid_date("04-32-2040"))  # Should print: False
print(valid_date("15-01-2012"))  # Should print: False
print(valid_date(""))  # Should print: False
```

This script should correctly validate dates based on the provided rules. Please note that this assumes that the input date string is in the format "mm-dd-yyyy" and may need to be modified if other date formats are to be accepted.