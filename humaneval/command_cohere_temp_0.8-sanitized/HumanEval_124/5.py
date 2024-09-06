import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/\s](\d{2})[-/\s](\d{4})', date))
    
    # Month range checks
    if (mm < 1 or mm > 12) or (dd < 1 or dd > DEPTH[mm - 1]):
        return False
    
    # Year check
    if yyyy < 1900 or yyyy > 2050:
        return False
    
    return True
DEPTH = {
    1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
    4: 30, 6: 30, 9: 30, 11: 30,
    2: 29,
}