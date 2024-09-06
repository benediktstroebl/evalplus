import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False

    # Check if date string follows the format mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())

    # Check valid range for day and month
    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        return False
    if 1 <= month <= 12 and day < 1 or day > 31:
        return False

    # Check valid range for month
    if month == 2 and day > 29:
        return False

    return True