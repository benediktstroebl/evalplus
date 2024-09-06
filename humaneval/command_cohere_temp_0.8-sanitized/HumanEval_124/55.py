import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d|\d', date))
    
    # Checks for the date format and month/day ranges
    if (
        (dd < 1 or dd > 31) and 
        (dd < 1 or dd > 30) and 
        (dd < 1 or dd > 29)
    ):
        return False

    # Checks for month range between 1-12
    if (mm < 1 or mm > 12):
        return False

    return True