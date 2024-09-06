import re
def valid_date(date):
    """
    Validate a date string and return True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Validate day and month
    max_day = [None, 31, 29, 31, 30, 31, 30, 31, 29, 31, 30, 31][mm-1]
    if dd < 1 or dd > max_day:
        return False

    # Validate year
    if 2000 <= yyyy <= 2030:
        return True
    else:
        return False