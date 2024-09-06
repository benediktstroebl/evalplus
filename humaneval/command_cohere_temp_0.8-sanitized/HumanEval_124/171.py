import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Month checks
    if (mm < 1 or mm > 12) or (dd < 1 or dd > diary_days(mm)):
        return False
    
    # Year check
    if yyyy < 1900 or yyyy > 2050:
        return False
    
    return True
def diary_days(month):
    # The number of days in a month varies outside the standard range.
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    else:  # month is 2 - special case
        return 29
date = '06-04-2020'