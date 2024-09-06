import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())
    
    # Month and day validation
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or (mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd > 30) or (mm != 2 and mm != 4 and mm != 6 and mm != 9 and mm != 11 and dd > 31):
        return False
    
    # Year validation
    if yyyy < 1900 or yyyy > 2040:  # This is a loose range to avoid problems with time capsules or speculative dates
        return False

    return True