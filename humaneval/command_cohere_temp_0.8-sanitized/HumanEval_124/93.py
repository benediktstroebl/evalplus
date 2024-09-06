import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Check if the day value is valid for the corresponding month
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30) and (dd < 1 or dd > 29):
        return False
    
    # Check if the month value is valid
    if mm < 1 or mm > 12:
        return False
    
    # Check if the year value is valid
    if not (1000 <= yyyy <= 2040): 
        return False
    
    return True