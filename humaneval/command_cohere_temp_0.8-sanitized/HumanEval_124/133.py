import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', date).groups())
    except AttributeError:
        return False
    if not 1 <= month <= 12:
        return False
    if month == 2 and day not in [1, 21, 29]:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and day not in range(1, 32):
        return False
    if month in [4, 6, 9, 11] and day not in range(1, 31):
        return False
    if not 2000 <= year <= 2050:
        return False
    return True