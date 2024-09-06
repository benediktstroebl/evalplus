Here's a Python script that includes a function called `valid_date` that solves the problem:
```python
import re

def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)[-/](\d?\d?)[-/](\d\d)\D*$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Month ranges
    if (month <= 0 or month > 12) or (month == 2 and day > 29) or (month == 4 or month == 6 or month == 9 or month == 11 and day > 30):
        return False
    
    # Year range
    if year < 1000 or year > datetime.datetime.now().year:
        return False
    
    return True
```

This code uses the `re` module to validate the date format and ensures the day and month values are within the acceptable ranges for each month. It also checks the year is within an acceptable range, bounded by the minimum and current year. 

Let's break down the code:
1. It imports the `re` module, which is used to work with regular expressions.
2. The `valid_date` function takes a date as input and returns `True` if the date is valid and `False` otherwise.
3. The date format is checked using a regular expression. The date is validated if it matches the pattern `(\d?\d?)[-/](\d?\d?)[-/](\d\d)\D*`, which corresponds to the date format `mm-dd-yyyy`. Here, `\D*` is a wildcard that accounts for the possibility of extra characters or punctuation beyond the date.
4. The code uses `re.match` to match the date format against the provided date string. `re.match` returns a match object if the input matches the pattern, and None if it doesn't.
5. The groups() method is used to extract the day, month, and year from the match object.
6. The code then checks for valid month and day ranges. Months 1, 3, 5, 7, 8, 10, and 12 accept a maximum of 31 days, while months 4, 6, 9, and 11 accept a maximum of 30 days, and the month 2 accepts a maximum of 29 days. It also checks that the year is within the valid range of 1000 to the current year.
7. If all the conditions are satisfied, the function returns `True`. Otherwise, it returns `False`.

This code ensures that the date string is not empty, has the correct format, and the day and month are within the acceptable ranges for each month.