Here's a Python script that implements the `valid_date` function described in the markdown code block:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r'(\d{2})-(\d{1,2})-(\d{4})', date)
    
    if not date_parts:
        return False
    
    year, month, day = date_parts.groups()
    
    # Validate day value
    if 1 <= int(day) <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= int(day) <= 31
        elif month in [4, 6, 9, 11]:
            return 1 <= int(day) <= 30
        elif month == 2:
            return 1 <= int(day) <= 29
        else:
            return False
    else:
        return False
    
    # Validate month value
    if 1 <= int(month) <= 12:
        return True
    else:
        return False
    
    # Validate year value
    date_parts = re.match(r'(\d{2})-(\d{1,2})-(\d{4})', date)
    
    if not date_parts:
        return False
    
    year, month, day = date_parts.groups()
    
    return 2000 <= int(year) <= 2030

# Test cases
print(valid_date('06-04-2020')) # Should print True
print(valid_date('06/04/2020'))  # Should print False
print(valid_date('03-11-2000'))  # Should print True
print(valid_date('15-01-2012'))  # Should print False
print(valid_date('04-0-2040'))   # Should print False
```

This script uses regular expressions to validate various aspects of the date string, including format, month, day, and year. 

It also assumes that the year format in the provided date strings is in the format `YYYY` (e.g., "2020", "2000"), which aligns with the provided examples. If the year format differs, the validation will not work as expected. 

Please keep in mind that date validation can be more complex in real-world scenarios, this solution addresses the specified problem statement. 

The code includes test cases to help demonstrate its behavior and ensure it's functioning correctly. 

Let me know if further clarification is necessary.