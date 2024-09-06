import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Month range validation
    if (dd<1 or dd>31) and (dd<1 or dd>30) and (dd<1 or dd>29):
        return False
    
    # Year and century validation
    if not (1000<=yyyy<=3000):
        return False
    
    return True