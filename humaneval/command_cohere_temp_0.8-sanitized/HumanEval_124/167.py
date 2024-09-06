import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or ((mm == 2) and (dd < 1 or dd > 29)) or ((mm == 4 or mm == 6 or mm == 9 or mm == 11) and (dd < 1 or dd > 30)):
        return False
    
    # Day check
    if dd < 1 or dd > (mm == 2 and dd <= 29) or dd > 31:  # Adjust the 31 to 30, 29, 28, etc based on the month
        return False
    
    # Year check
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    return True