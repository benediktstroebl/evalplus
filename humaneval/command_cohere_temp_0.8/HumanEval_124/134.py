Here's a Python script that defines a function to validate a date string based on the given rules:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.match(r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', date).groups())
    
    # Check if the date is within valid range
    max_days = [None, 30, 29, 31, 30, 31, 31, 30, 31, 30, 31]
    if mm < 1 or mm > 12 or dd < 1 or dd > max_days[mm - 1] or yyyy < 2000:
        return False
    
    return True

# Test cases
print(valid_date('06-04-2020'))  # Should print True
print(valid_date('03-11-2000'))  # Should print True
print(valid_date('06/04/2020'))  # Should print False
print(valid_date('15-01-2012'))  # Should print False
print(valid_date('04-0-2040'))  # Should print False
```

This script uses regular expressions to validate the date format and extract year, month, and day values from the input date string. The function then checks whether the date is within the valid range for each component. Finally, it returns `True` if all checks pass, and `False` otherwise. 

The test cases correctly reflect the constraints stated in the problem and should help you verify the correctness of the function. You can add more test cases to cover other edge cases.