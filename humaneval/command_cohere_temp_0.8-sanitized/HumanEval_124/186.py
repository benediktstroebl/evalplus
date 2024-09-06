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
        if day not in range(1, 29):
            return False
    elif month in (1, 3, 5, 7, 8, 10, 12) and day not in range(1, 32):
        return False
    elif month in (4, 6, 9, 11) and day not in range(1, 31):
        return False
    
    # Check month validity
    if month not in range(1, 13):
        return False
    
    # Check year validity
    if year < 1000:
        return False
    
    return True