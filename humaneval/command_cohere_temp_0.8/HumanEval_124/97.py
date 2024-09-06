Here's a Python script that defines a function to validate a date string according to the given problem statement:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Validate the date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False
    
    # Extract month, day, and year from the match
    month, day, year = map(int, match.groups())
    
    # Validate month and day
    if 1 <= month <= 12:
        if (month == 2 and day >= 1 and day <= 29) or
           (month != 2 and day >= 1 and day <= 31):
            return True
    
    return False

# Test cases
print(valid_date("06-04-2020"))  # Should print: True
print(valid_date("03-11-2000"))  # Should print: True
print(valid_date("15-01-2012"))  # Should print: False
print(valid_date("04-0-2040"))  # Should print: False
print(valid_date("06/04/2020"))  # Should print: False
print(valid_date(""))  # Should print: False
```

This script uses the re module to validate the date format and a regular expression to ensure that the date provided follows the expected format `mm-dd-yyyy`. It then checks if the month and day values are within the acceptable ranges. The script includes test cases to help verify its correctness. 

The function outputs True for valid dates and False for invalid ones. 

Note: This solution utilizes regular expressions to validate the format and therefore, is case-sensitive, so it would incorrectly reject dates like '06/04/2020' because the format includes capitalized letters. If the date format does not include any capitalized letters and is case-sensitive, the solution is appropriate, otherwise it may require additional adjustments.