import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Validate the date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-[\d]{2}-[\d]{4}$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())
    
    # Validate the day and month ranges
    if month == 2:
        if day not in range(1, 29):
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12] :
        if day not in range(1, 32):
            return False
    else:
        if day not in range(1, 31):
            return False
    
    # Validate the year range
    if year < 2000 or year > 2030:
        return False
    
    return True