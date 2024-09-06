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
    if dd < 1 or dd > VALID_DAYS[mm]:
        return False
    
    # Validate year
    if yyyy < 1900 or yyyy > datetime.datetime.now().year:
        return False
    
    return True
VALID_DAYS = {
    1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
    4: 30, 6: 30, 9: 30, 11: 30,
    2: 29,
}