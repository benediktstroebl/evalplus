Here's a Python script that implements the `valid_date` function described in the prompt:
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
        if month in ['1', '3', '5', '7', '8', '10', '12']:
            return 1 <= int(day) <= 31
        elif month in ['4', '6', '9', '11']:
            return 1 <= int(day) <= 30
        elif month == '2':
            return 1 <= int(day) <= 29
    else:
        return False
    
    # Validate month value
    if 1 <= int(month) <= 12:
        return True
    else:
        return False
    
    # Validate year value
    return 2000 <= int(year) <= 2030

# Test cases
print(valid_date('06-04-2020')) # Should print True
print(valid_date('03-11-2000')) # Should print True
print(valid_date('15-01-2012')) # Should print False
print(valid_date('04-0-2040')) # Should print False
print(valid_date('06/04/2020')) # Should print False
print(valid_date('')) # Should print False
```

This script uses regular expressions to validate various aspects of the date string, including format, month, day, and year. 

The `re.match` function is used to ensure the date string matches the expected format. The groups extracted from the match are then used to validate the day and month values. Finally, the overall validity of the date is determined based on these checks. 

The script also includes some simple tests that cover a variety of scenarios. The function should return `True` for valid dates and `False` for invalid ones. Feel free to add more tests to cover more edge cases if necessary. 

This way, the script ensures that the date string is not empty, is in the right format, and satisfies all the rules mentioned in the prompt.  The script is standalone and doesn't rely on external modules, making it self-contained.