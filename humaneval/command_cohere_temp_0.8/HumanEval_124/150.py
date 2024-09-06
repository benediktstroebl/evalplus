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
    else:
        if day < 1 or day > 29:
            return False
    
    # Check for valid month range
    if month < 1 or month > 12:
        return False
    
    # Check for valid date format
    if not re.match(r'^(\d{2})[-/](\d{1,2})[-/](\d{4})$', date):
        return False
    
    return True
```

This code uses regular expressions to validate the date against the specified format, ensuring the date components are within the acceptable ranges for months and days. Let's break down the key components:
1. **Date Format Validation:**
   A regular expression `r'(\d{2})[-/](\d{1,2})[-/](\d{4})'` is used to match the date string against the expected format `mm-dd-yyyy`. This ensures the date components are separated by dashes or slashes and in the correct order.
2. **Date Components Extraction:**
   The `re.match` function is used to match the date string against the format regular expression. The `groups()` method of the match object returns a list of all the captured groups in the order they were captured. In this case, it should capture three groups: year, month, and day.
3. **Valid Day and Month Ranges:**
   The code defines tuples `(month, day)` representing acceptable day ranges for each month. These are used to check if the captured day is within the valid range for the corresponding month. If the month and day combination is not within any of the predefined ranges, it checks for a maximum of 29 days for February.
4. **Valid Month Range:**
   The code checks if the captured month is within the valid range of 1 to 12.
5. **Validation Passed:**
   If all the above conditions pass, the function returns `True`, indicating a valid date; otherwise, it returns `False`.

You can use this `valid_date` function to validate date strings against the specified format and criteria.