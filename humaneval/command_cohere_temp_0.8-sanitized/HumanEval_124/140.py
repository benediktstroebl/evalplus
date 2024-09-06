import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month and day validation
    if mm < 1 or mm > 12:
        return False
    max_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mm == 2:
        max_days = [29] * 4 + max_days[:-1]
    elif mm in [4, 6, 9, 11]:
        max_days = [30] * 3 + max_days[:-1]
    if dd < 1 or dd > max_days[mm - 1]:
        return False
    
    # Year validation
    if yyyy < 1900 or yyyy > 3000:
        return False
    
    return True