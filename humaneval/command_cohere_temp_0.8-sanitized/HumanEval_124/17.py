import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d?\D?\d\d?\D?\d\d?\D?\d\d?\D?\d\d?\D?\d\d?', date))
    if not (1 <= mm <= 12):
        return False
    if (mm == 2 and (dd < 1 or dd > 29)) or (mm != 2 and (dd < 1 or dd > 30)):
        return False
    if not (1000 <= yyyy <= 3000):
        return False
    if not (1 <= dd <= 31):
        return False
    return True