import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d\d?)-[\d\d]-[\d\d\d\d]$", date)
    if not match:
        return False
    d, m, y = map(int, match.groups())
    if 1 <= m <= 12:
        if (m == 2 and d != 29) or (m not in [2, 4, 6, 9, 11] and d not in range(1, 32)):
            return False
        return True
    else:
        return False