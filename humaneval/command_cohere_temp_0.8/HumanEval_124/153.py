Here's a Python script that implements the `valid_date` function described in the problem:
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
    
    year, month, day = map(int, date_parts.groups())
    
    # Check if the date is within valid range
    if 1 <= month <= 12:
        if (month == 2 and day >= 1 and day <= 29) or
           (month != 2 and day >= 1 and day <= 31):
            return True
        else:
            return False
    else:
        return False
    
    return False
```

This code uses the re module to handle the regular expression matching to extract the year, month, and day parts from the date string. The function then checks if the extracted values are within the valid range for each part. 

The function returns True if all the conditions are met, meaning that the date is valid. Otherwise, it returns False. You can use it in your code to check if a given date string is valid according to the specified rules.