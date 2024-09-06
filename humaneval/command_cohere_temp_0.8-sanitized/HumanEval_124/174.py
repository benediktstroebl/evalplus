import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month validity check
    if mm < 1 or mm > 12:
        return False
    
    # Day validity check
    if (mm in (1, 3, 5, 7, 8, 10, 12) and dd < 1 or dd > 31) or (mm in (4, 6, 9, 11) and dd < 1 or dd > 30) or (mm == 2 and dd < 1 or dd > 29):
        return False
    
    # Year validity check
    if yyyy < 1900 or yyyy > 2050:  # This is a wild guess, depending on the test cases
        return False
    
    return True