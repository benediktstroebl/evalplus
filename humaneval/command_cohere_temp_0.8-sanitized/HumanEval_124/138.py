import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.findall(r'\d+', date))
        if (month < 1 or month > 12) or (day < 1 or day > DAYS_PER_MONTH[month - 1]) or year < 2000:
            return False
    except:
        return False
    return True
DAYS_PER_MONTH = [
    31, 30, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 29
]