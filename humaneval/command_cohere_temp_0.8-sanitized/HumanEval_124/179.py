import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d{4})", date).groups())
    
    # Month and day validation
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or (mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd > 30) or (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12 and dd > 31):
        return False
    
    # Year validation
    if yyyy < 1900 or yyyy > 2030:
        return False
    
    return True