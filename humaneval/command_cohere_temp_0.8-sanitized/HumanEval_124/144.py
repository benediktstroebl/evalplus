import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())

    if not (1 <= mm <= 12):
        return False
    if (mm == 2 and dd != 29) or (mm != 2 and dd not in [30, 31]):
        return False
    if not (1 <= dd <= 31):
        return False
    if not (1000 <= yyyy <= 9999):
        return False
    
    return True