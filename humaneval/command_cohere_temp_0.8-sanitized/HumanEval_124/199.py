import re
def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.match(r'(\d{4})-(\d\d)-(\d\d)', date).groups())
    
    # Check if the date is within valid range
    max_days = [None, 30, 29, 31, 30, 31, 31, 30, 31, 30, 31]
    if mm < 1 or mm > 12 or dd < 1 or dd > max_days[mm - 1] or yyyy < 2000:
        return False
    
    return True