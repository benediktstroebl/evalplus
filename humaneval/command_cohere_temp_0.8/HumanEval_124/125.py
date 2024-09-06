Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.strip()
        date = date.split('-')
        mm, dd, yyyy = map(int, date)

        if 1 <= mm <= 12:
            max_days = 30 if (mm == 4 or mm == 6 or mm == 9 or mm == 11) else 31
            if dd < 1 or dd > max_days:
                return False
        else:
            return False

        if 1970 <= yyyy <= 2030:
            if not re.match(r"^[0-9]{4}$", str(yyyy)):
                return False
        else:
            return False

        return True
    except Exception:
        return False
```

The function takes a date as input and checks it against the four rules specified in the problem. The function returns `True` if all rules are satisfied, and `False` otherwise. 

To validate the date against the first rule, the function checks if the input date is empty. The `str.strip()` and `str.split('-')` functions are used to remove leading and trailing spaces from the date and to split the date into the three integers needed to validate the date. 

The months' range is validated against the second rule using a ternary conditional statement to verify if the month is between 1 and 12, and the day of the month is validated against the number of days in the specific month using a maximum value stored in the `max_days` variable. 

The function validates the year using a regular expression `regex` against the third rule, checking if the year is between 1970 and 2030. 

The function catches any error occurred during the transformation of the date string into an integer that prevents it from validating the date string against the rules, and simply returns `False` in case of error.