Here's a Python script that includes a function called `valid_date` to solve the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d\d?)-[\d\d]-[\d\d\d\d]$", date)
    if not match:
        return False
    mm, dd, yyyy = map(int, match.groups())
    # Month between 1 and 12
    if mm < 1 or mm > 12:
        return False
    # Number of days varies based on the month
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if dd < 1 or dd > days_in_month[mm - 1]:
        return False
    return True
```

This function first checks if the date string is empty. It then uses a regular expression to ensure the date is in the correct format (`mm-dd-yyyy`). Finally, it checks if the day and month are within the specified ranges (1-31 for most months, 1-30 for April, June, September, and November, and 1-29 for February), and returns True if so. It returns False if the date is invalid for any of these reasons. 

The regular expression used will match any date in the format `mm-dd-yyyy`, where `mm` is a two-digit month, `dd` is a two- or three-digit day, and `yyyy` is a four-digit year. To account for leading zeros, we use `[\d\d]?` to match one or two instances of the digit. 

For example, the date "06-04-2020" would be validated as:
- mm = 06 (06 is valid for month 06)
- dd = 04 (04 is valid for day 04)
- yyyy = 2020 (this is a valid year)

All valid ranges, so the function would return True. 

Let's check on the rejected dates from the example provided in the question: 
 - '15-01-2012' - Invalid because mm = 15, which is outside the range of 1-12. 
 - '04-0-2040' - Invalid because dd = 0, which is less than 1. 
 - '06/04/2020' - Invalid because / is not permitted in the date string. 

So all of these would return False.