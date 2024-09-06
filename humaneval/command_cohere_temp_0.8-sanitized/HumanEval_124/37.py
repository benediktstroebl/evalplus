import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Validate day and month
    if dd < 1 or dd > 31:
        return False
    if (mm == 2 and dd != 29) or (mm not in [2,4,6,9,11] and dd > 30) or mm < 1 or mm > 12:
        return False
    
    # Validate year
    if yyyy < 1900 or yyyy > 2040:  # This range can be adjusted as needed
        return False
    
    return True