import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    date = date.strip()
    
    if not date:
        return False
    
    match = re.match(r"^(\d\d?)[-/](\d\d?)[-/](\d\d\d\d)$", date)
    
    if not match:
        return False
    
    day = int(match.group(2))
    month = int(match.group(1))
    year = int(match.group(3))
    
    if month < 1 or month > 12:
        return False
    
    if month == 2:
        if day not in range(1, 32):
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day not in range(1, 31):
            return False
    else:
        if day not in range(1, 33):
            return False
    
    return True