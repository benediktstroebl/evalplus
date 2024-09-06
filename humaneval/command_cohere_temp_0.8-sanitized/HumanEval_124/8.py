import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)[-/](\d?\d?)[-/](\d\d\d\d)$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Dates between 1-31
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8
        or month == 10 or month == 12) and day < 1 or day > 31:
        return False
    
    # Dates between 4-,30
    if month == 4 or month == 6 or month == 9 or month == 11 and day < 1 or day > 30:
        return False
    
    # Dates between 2-29
    if month == 2 and day < 1 or day > 29:
        return False
    
    if month < 1 or month > 12:
        return False
    
    return True