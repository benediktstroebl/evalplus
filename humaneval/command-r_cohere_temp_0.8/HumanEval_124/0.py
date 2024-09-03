```python
import re


def valid_date(date):
    """Validate a date string based on multiple conditions.

    Rules:
    1. Date string should not be empty.
    2. Days: 1-31 for Jan, Mar, May, Jul, Aug, Oct, Dec. 1-30 for Apr, Jun, Sep, Nov. 1-29 for Feb.
    3. Months: 1-12.
    4. Format: mm-dd-yyyy

    Returns:
        bool: True if valid, False otherwise.
    """
    # Check if date string matches the required format
    if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
        return False

    month, day, year = map(int, date.split("-"))

    # Validate days and months
    if (
        (month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31))
        or (month in [4, 6, 9, 11] and (day < 1 or day > 30))
        or (month == 2 and (day < 1 or day > 29))
        or month < 1 or month > 12
    ):
        return False

    return True
```