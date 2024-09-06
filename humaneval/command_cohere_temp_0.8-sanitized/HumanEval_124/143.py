import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Validate day and month
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or (mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd > 30) or (mm != 2 and mm != 4 and dd > 31):
        return False
    
    # Validate year
    if yyyy < 2000 or yyyy > 2040:  # Adjust the range according to your requirement
        return False

    return True