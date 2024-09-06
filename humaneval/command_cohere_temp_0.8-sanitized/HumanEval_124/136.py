import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month range validation
    if (mm < 1 or mm > 12) or  ((mm == 2) and (dd != 1 and dd != 29)) or ((mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd != 1 and dd > 30):
        return False
    
    # Day range validation
    if dd < 1 or dd > (mm == 2 and dd <= 29) or dd > 31 - ((mm == 2 and dd > 28) or 0):
        return False
    
    # Year validation
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    return True