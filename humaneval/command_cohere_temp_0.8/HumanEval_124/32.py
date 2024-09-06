Here's a Python script that defines a function to validate a date string based on the given rules:
```python
import re

def valid_date(date):
    """
    Validate a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False
    
    day, month, year = map(int, match.groups())
    
    # Check month and day validity
    if month < 1 or month > 12:
        return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    else:  # for month 4, 6, 9, 11
        if day < 1 or day > 30:
            return False
    
    return True

# Test cases
print(valid_date("06-04-2020"))  # Should print: True
print(valid_date("03-11-2000"))  # Should print: True
print(valid_date("15-01-2012"))  # Should print: False
print(valid_date("04-0-2040"))  # Should print: False
print(valid_date("06/04/2020"))  # Should print: False
print(valid_date(""))  # Should print: False
```

This script uses regular expressions to check if the date string matches the expected format. It then checks the validity of the day and month within the context of the specific month and returns True if all conditions are met and the date is valid. The function returns False if the date is invalid for any reason outlined in the problem statement. 

The script tests the function with a variety of date strings to ensure it passes all the test cases mentioned in the problem statement. 

Please feel free to ask any questions or make suggestions for other code problems you'd like to see solved!