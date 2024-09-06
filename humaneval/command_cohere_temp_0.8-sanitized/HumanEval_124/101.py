import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.findall(r'\d+', date)[:3])
        if (month, day) < (1, 1) or (month, day) > (12, 31) or \
           (month == 2 and day > 29) or \
           (month in [4, 6, 9, 11] and day > 30) or \
           year < 2000 or year > 2040:
            return False
        return True
    except:
        return False