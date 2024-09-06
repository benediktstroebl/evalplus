import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d{4})", date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or (
            (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30) or (
            mm == 2 and dd > 29):
        return False
    
    # Day checks
    if dd < 1 or dd > (mm == 2 and dd <= 29) or dd > 31:  # Consider leap years for month 2
        return False
    
    # Year checks
    if yyyy < 1900 or yyyy > (mm == 2 and dd <= 29) or yyyy > 2050:  # Consider leap years for month 2
        return False
    
    return True