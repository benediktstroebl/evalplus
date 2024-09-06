import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Validate day and month
    if mm < 1 or mm > 12:
        return False
    elif mm == 2:
        if dd < 1 or dd > 29:
            return False
    elif mm in [4, 6, 9, 11]:
        if dd < 1 or dd > 30:
            return False
    else:
        if dd < 1 or dd > 31:
            return False
    
    # Validate year
    if yyyy < 1900 or yyyy > 2050: 
        return False
    
    # Format validation
    if date.count('-') == 2 and date.count('/') == 0 and re.match(r"^(0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])[-/](\d{4})$", date):
        return True
    elif date.count('/') == 2 and date.count('-') == 0 and re.match(r"^(\d{2})/(__[0-6])/(\d{4})$", date):
        return True
    else:
        return False