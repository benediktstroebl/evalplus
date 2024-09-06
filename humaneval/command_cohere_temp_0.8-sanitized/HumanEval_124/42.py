import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Check format
    if not re.match(r"^(\d\d?)-[\d\d]-[\d\d\d\d]$", date):
        return False
    
    # Extract day, month, and year
    day, month, year = map(int, date.split('-')[0:3])
    
    # Check month and day validity
    if month < 1 or month > 12:
        return False
    elif month == 2 and day > 29:
        return False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False

    return True