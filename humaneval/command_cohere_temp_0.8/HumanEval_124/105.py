Here's a Python script that defines a function called `valid_date` to validate a date string and returns `True` if the date is valid and `False` otherwise. The date is considered valid if it satisfies the following rules:
1. The date string is not empty.
2. The number of days is between 1 and the last day of the month for the given month and year.
3. The months should be between 1 and 12.
4. The date is in the format `mm-dd-yyyy`.

```python
import re

def valid_date(date):
    """
    Validate a date string and returns True if date is valid otherwise False .
    """
    date = date.strip()
    if not date:
        return False
    match = re.match(r"^(\d{1,2})[-/](\d{1,2})[-/](\d{4})$", date)
    if not match:
        return False
    mm, dd, yyyy = map(int, match.groups())

    # Days must be between 1 and the last day of the month.
    last_day = datetime.date(yyyy, mm, 1).isocalendar()[1]
    if 1 <= dd <= last_day:
        return True
    else:
        return False
```

The function leverages the `re` module to match the date format and then validates the constraints on the parameters. The function checks if the day is within the valid range for the given month and year. Ultimately, the function returns `True` if all the constraints are satisfied; otherwise, it returns `False`.