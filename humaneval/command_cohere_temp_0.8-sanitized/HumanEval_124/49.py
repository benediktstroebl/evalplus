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
    if not (1 <= m <= 12):
        return False
    if m == 2 and not (1 <= d <= 29):
        return False
    if m != 2 and not (1 <= d <= 31):
        return False
    return True