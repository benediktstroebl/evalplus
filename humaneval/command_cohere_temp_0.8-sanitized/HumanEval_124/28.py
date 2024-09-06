import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r'(\d{2})[-/](\d{1,2})[-/](\d{4})', date)
    
    if not date_parts or date_parts.groups() != 3:
        return False
    
    year, month, day = map(int, date_parts.groups())
    
    # Check for valid day and month ranges
    if (month, day) in [(1, 31), (3, 31), (5, 31), (7, 31), (8, 31), (10, 31), (12, 31)]:
        if day < 1 or day > 31:
            return False
    elif (month, day) in [(4, 30), (6, 30), (9, 30), (11, 30)]:
        if day < 1 or day > 30:
            return False
    elif month == 2 and day < 1 and day > 29:  # Handle Feb 29th
        return False
    
    # Check for valid month range and correct two-digit format
    if month < 1 or month > 12:
        return False
    
    # Check for valid year format
    if year < 1000 or year > datetime.datetime.now().year:
        return False
    
    return True