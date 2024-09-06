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
    elif mm == 2:
        if dd < 1 or dd > 29:
            return False
    elif mm in [4, 6, 9, 11]:
        if dd < 1 or dd > 30:
            return False
    else:  # Months 1, 3, 5, 7, 8, 10, 12
        if dd < 1 or dd > 31:
            return False

    # Date within range 2000-2100
    if yyyy < 2000 or yyyy > 2100:
        return False
    
    return True