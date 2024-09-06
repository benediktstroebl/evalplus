import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', date).groups())
        if (month, day) < (1, 1) or (month, day) > (12, 31) or \
           (month == 2 and day > 29) or \
           (month in [4, 6, 9, 11] and day > 30) or \
           year < 2000 or year > 2040:
            return False
    except AttributeError:  # Raise this error if any of the groups cannot be matched
        return False
    return True