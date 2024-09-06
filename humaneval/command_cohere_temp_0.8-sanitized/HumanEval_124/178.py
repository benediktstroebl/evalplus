import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month range validation
    if (mm < 1 or mm > 12) or  (
        (mm == 2 and dd != 1) or 
        (mm in [4, 6, 9, 11] and dd > 30) or 
        (mm in [1, 3, 5, 7, 8, 10, 12] and dd > 31)
    ):
        return False
    
    # Year validation
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    # Day validation
    if (dd < 1 or dd > 31) or (dd < 1 or dd > 30):
        return False
    
    return True