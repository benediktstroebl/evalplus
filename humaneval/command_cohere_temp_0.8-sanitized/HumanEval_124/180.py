import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False
    
    mm, dd, yyyy = map(int, match.groups())
    
    # Check day validity
    if mm == 2:
        if dd < 1 or dd > 29:
            return False
    elif mm in [1, 3, 5, 7, 8, 10, 12] :
        if dd < 1 or dd > 31:
            return False
    elif mm in [4, 6, 9, 11] : 
        if dd < 1 or dd > 30:
            return False
    
    # Check month validity
    if mm < 1 or mm > 12:
        return False
    
    # If all checks passed, the date is valid
    return True