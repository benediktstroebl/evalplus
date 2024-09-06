import re
def valid_date(date):
    """
    Validate a date string and return True if the date is valid.
    Otherwise, return False.
    """
    # Pattern to match the date format
    date_format = re.compile(r"^(\d{2})[-/](\d{2})[-/](\d{4})$")

    # Checking if the date string is empty
    if not date:
        return False

    # Checking the date format
    if not date_format.match(date):
        return False

    year, month, day = map(int, date.split('-'))

    # Checking the range of the day for each month
    if month == 2 and day not in range(1, 29):
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 31):
        return False
    elif month in [4, 6, 9, 11] and day not in range(1, 30):
        return False

    # Checking the range of the month
    if month < 1 or month > 12:
        return False

    return True