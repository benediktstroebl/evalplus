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
    date_parts = re.match(r'(\d{2})[-/](\d{1,2})[-/](\d{4})', date)
    
    if not date_parts or date_parts.groups() != 3:
        return False
    
    year, month, day = map(int, date_parts.groups())
    
    # Check for valid day and month ranges
    if (month, day) in [(1, 31), (3, 31), (5, 31), (7, 31), (8, 31), (10, 31), (12, 31)]:
        if day < 1 or day > 31:
            return False
    elif (month, day) in [(4, 30), (6, 30), (9, 30), (11, 30)]:
        if day < 1 or day > 30:
            return False
    elif month == 2 and day < 1 and day > 29:  # Handle Feb 29th
        return False
    
    # Check for valid month range and correct two-digit format
    if month < 1 or month > 12:
        return False
    
    # Check for valid year format
    if year < 1000 or year > datetime.datetime.now().year:
        return False
    
    return True

# Test cases
print(valid_date('03-11-2000'))  # Should print True
print(valid_date('15-01-2012'))  # Should print False
print(valid_date('04-0-2040'))  # Should print False
print(valid_date('06-04-2020'))  # Should print True
print(valid_date('06/04/2020'))  # Should print False
```
This code uses a regular expression to validate the date format and checks the validity of the date components (day and month) against the specified rules. Finally, it returns True if all checks pass, and False otherwise. 
The regular expression `r'(\d{2})[-/](\d{1,2})[-/](\d{4})'` is used to match the date format mm-dd-yyyy, capturing the two-digit month, one-to-two-digit day, and four-digit year. 

The function will return `True` for any date that fits the `mm-dd-yyyy` format, has valid day and month ranges, and has a valid year range. 

This code assumes that the date string follows the British date format (day before month, e.g., 03-11-2000). If the date string follows another format (e.g., 11-03-2000), it would not be considered valid and return `False`. 

Let's break down the key functionalities of the `valid_date` function:
1. **Date Format Validation**:
   The code begins by checking if the date string is not empty. It does this using the re.match routine that matches the date format mm-dd-yyyy. This routine also extracts the year, month, and day from the date string. 

2. **Valid Day and Month Ranges**:
   The function then checks the validity of the day and month ranges. The list of tuples `(month, day)` checks the range of days for each month. It specifically checks for