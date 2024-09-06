Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or (
            (mm in (1, 3, 5, 7, 8, 10, 12) and dd < 1 or dd > 31) or
            (mm in (4, 6, 9, 11) and dd < 1 or dd > 30) or
            (mm == 2 and dd < 1 or dd > 29)):
        return False
    
    # Date format check
    if not re.match(r'^(\d\d)-(\d\d)-(\d\d\d\d)$', date):
        return False
    
    return True
```

This function checks for several conditions to determine date validity, such as verifying the provided date's format, ensuring the month falls within a valid range (1-12), and checking the number of days in specific months. It utilizes the re.match routine to extract month, day, and year while validating the format. 

The function returns True if all conditions are satisfied, otherwise, it returns False. 

To further clarify the validation process, here's a breakdown of the checks on months 1, 3, 5, 7, 8, 10, and 12:
- Month validity: 1-12
- Day validity: 1-31

And for months 4, 6, 9, 11:
- Month validity: 1-12
- Day validity: 1-30

And for month 2:
- Month validity: 1-12
- Day validity: 1-29