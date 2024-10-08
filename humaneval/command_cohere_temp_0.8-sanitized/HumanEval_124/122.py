import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())
    
    # Validate day and month
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30) and (dd < 1 or dd > 29):
        return False
    
    if (mm < 1 or mm > 12):
        return False
    
    # Validate year
    if yyyy < 1000 or yyyy > 2030:
        return False
    
    return True