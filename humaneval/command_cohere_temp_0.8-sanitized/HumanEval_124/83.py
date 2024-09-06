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
    mm, dd, yyyy = map(int, match.groups())
    # Month between 1 and 12
    if mm < 1 or mm > 12:
        return False
    # Number of days varies based on the month
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if dd < 1 or dd > days_in_month[mm - 1]:
        return False
    return True