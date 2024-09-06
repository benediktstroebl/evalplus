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
    else:
        if dd < 1 or dd > 31:
            return False
    
    # Year check
    if yyyy < 1900 or yyyy > 2020:  # This range can be adjusted as needed
        return False
    
    return True
date = '06-04-2020'