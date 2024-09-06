import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d|\d', date))

    if not (1 <= mm <= 12):
        return False

    # Determine number of days based on the month
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if not (1 <= dd <= days_in_month[mm - 1]):
        return False

    # Check date range
    if (yyyy < 2000 or yyyy > 2040) or (yyyy == 2000 and mm < 3):
        return False

    return True