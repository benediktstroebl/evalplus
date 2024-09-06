import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.match(r'(\d{4})-(\d{2})-(\d{2})', date).groups())
    
    # Check if the date is in the correct format
    if not re.match(r'^(\d{2})-(\d{2})-(\d{4})$', date):
        return False
    
    # Check month and day validity
    if mm < 1 or mm > 12:
        return False
    if mm == 2 and dd > 29:
        return False
    if mm != 2 and dd < 1 or dd > 31:
        return False
    
    # Check year validity (assuming 2000-2099 is considered valid)
    if yyyy < 2000 or yyyy > 2099:
        return False
    
    return True