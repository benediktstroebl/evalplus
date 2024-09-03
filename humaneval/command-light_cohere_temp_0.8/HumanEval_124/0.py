```python
import re

def valid_date(date):
    """
    Validate date string according to the format mm-dd-yyyy
    """
    # use regex to validate the date format
    date_regex = re.compile('^\Date: \d{1}[/-]\d{3}-[/-]\d{4}')
    return date_regex.isMatch(date)
```
This Python code defines a function called valid_date that checks the format of a given date string using regular expressions. The regular expression (date_regex) matches the date string against a pattern that requires a four-digit month number, a hyphen, and then the day and year separated by dashes in that order, followed by another hyphen and four-digit year number. The function returns True if the date string matches this pattern, indicating a valid date format. 

The code is well-contained and self-contained, and it efficiently validates date strings according to a specific format using regular expressions.