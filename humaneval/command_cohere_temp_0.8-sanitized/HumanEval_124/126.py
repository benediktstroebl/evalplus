import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Check day validity
    if month == 2:
        if day not in range(1, 32):
            return False
    else:
        if day not in range(1, 33):
            return False
    
    # Check month validity
    if month not in range(1, 13):
        return False
    
    return True