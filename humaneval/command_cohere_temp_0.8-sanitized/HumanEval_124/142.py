import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d{2}-\d{2}-\d{4}', date))
    
    # Validate day and month
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30):
        return False
    if (mm < 1 or mm > 12):
        return False
    
    # Validate year
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    return True