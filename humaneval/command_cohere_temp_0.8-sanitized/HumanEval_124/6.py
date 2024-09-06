import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month checks
    if mm < 1 or mm > 12:
        return False
    
    # Day checks
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if mm == 2 and dd > 29:
        return False
    elif mm in [1, 3, 5, 7, 8, 10, 12] and dd > 31:
        return False
    elif mm in [4, 6, 9, 11] and dd > 30:
        return False
    
    return True