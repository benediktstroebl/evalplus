Here's a Python script that implements the `valid_date` function described in the markdown code block:
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
           (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30) or (
           mm == 2 and dd > 29):
        return False

    # Day checks
    if dd < 1 or mm == 2 and dd > 29 or (mm != 2, 4, 6, 9, 11) and dd > 31:
        return False

    # Format check
    if not re.match(r'^(\d\d)-(\d\d)-(\d{4})$'.format(mm, dd, yyyy), date):
        return False

    return True
```

This code breaks down the date string into three parts: `mm` for month, `dd` for day, and `yyyy` for year. It utilizes a regular expression to parse these three numbers from the date string. The code then checks a number of conditions to ensure that the date is valid. These checks include confirming that the month is between 1 and 12, that the day is between 1 and the maximum number of days for the specific month (taking into account February's 29th day), and that the date string is formatted correctly. The function returns True if all the conditions are satisfied and the date is valid, and False otherwise. 

The regular expression `r'(\d\d)-(\d\d)-(\d\d\d\d)'` captures three groups of two digits (for the month, day, and year, respectively), and `^(\d\d)-(\d\d)-(\d{4})$` validates the date format. 

Note that this code assumes that the date string follows the format `mm-dd-yyyy` or `dd-mm-yyyy` and assumes years in the range 2000-2100. You may need to adjust the code for other date formats or year ranges.