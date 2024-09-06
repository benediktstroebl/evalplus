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
    if not re.match(r"^(\d{2})-[\d]{2}-[\d]{4}$", date):
        return False
    
    # Extract day, month, and year from the date string
    day, month, year = map(int, date.split('-')[0:3])
    
    # Validate day
    if 1 <= day <= 31:
        pass
    else:
        return False
    
    # Validate month
    if 1 <= month <= 12:
        pass
    else:
        return False
    
    # Validate year
    if 2000 <= year <= 2030:
        pass
    else:
        return False
    
    # Validate month-day combination
    if (month, day) in [(1,31), (3,31), (5,31), (7,31), (8,31), (10,31), (12,31)]:
        pass
    elif (month, day) in [(4,30), (6,30), (9,30), (11,30)]:
        pass
    else:
        return False
    
    return True
```

This code uses the `re` module to validate the date format and regular expressions. It ensures that the date components (day, month, and year) fall within the specified ranges. The script returns `True` if all checks pass, indicating a valid date, or `False` otherwise. 

Make sure to have the `re` module imported to run this code.