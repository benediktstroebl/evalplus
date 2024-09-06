import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d{4})", date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or (dd < 1 or dd > sum(range(1, 32)) if (mm == 4 or mm == 6 or mm == 9 or mm == 11) else (dd < 1 or dd > 31)):
        return False
    
    # Date format check
    if re.match(r"^(\d\d)-(\d\d)-(\d{4})$", date):
        return True
    else:
        return False