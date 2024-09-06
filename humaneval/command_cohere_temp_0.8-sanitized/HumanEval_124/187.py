import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Month range checks
    if (dd<1 or dd>31) and (mm in [1, 3, 5, 7, 8, 10, 12]):
        return False
    if (dd<1 or dd>30) and (mm in [4, 6, 9, 11]):
        return False
    if dd<1 or dd>29 and mm == 2:
        return False
    
    # Year and day range checks
    if mm<1 or mm>12:
        return False
    if yyyy<1000 or yyyy>3000:
        return False
    
    return True