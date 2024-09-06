import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract date components
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Check month and day validity
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
    
    # Check year validity (assume 2000-2099 are valid)
    if yyyy < 2000 or yyyy > 2099:
        return False
    
    return True
date = '06-04-2020'