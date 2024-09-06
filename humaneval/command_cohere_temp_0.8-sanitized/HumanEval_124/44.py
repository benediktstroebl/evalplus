import re
def valid_date(date):
    """
    Validate a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False
    
    day, month, year = map(int, match.groups())
    
    # Check month and day validity
    if month < 1 or month > 12:
        return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    else:  # for month 4, 6, 9, 11
        if day < 1 or day > 30:
            return False
    
    return True