import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d{2}|-|\d{4}', date))
    
    # Checks for the date format mm-dd-yyyy
    if '-' not in date or len(date) != 10:
        return False

    # Checks for month validation
    if mm < 1 or mm > 12:
        return False
    elif mm == 2:
        if dd < 1 or dd > 29:
            return False
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if dd < 1 or dd > 30:
            return False
    else:
        if dd < 1 or dd > 31:
            return False

    # Checks for day validation
    if dd < 1 or dd > 31:
        return False
    
    return True