import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Checks for the number of days and months
    if (
        (dd < 1 or dd > 31) and 
        (dd < 1 or dd > 30) and 
        (dd < 1 or dd > 29)
    ):
        return False

    if mm < 1 or mm > 12:
        return False
    
    # Date format check
    if re.match(r"^(\d\d)-(\d\d)-(\d\d\d\d)$", date):
        return True
    return False