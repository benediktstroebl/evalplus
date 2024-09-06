import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month is valid if it is between 1 and 12
    if mm < 1 or mm > 12:
        return False
    
    # If the date is in February, the day is valid if it's between 1 and 29
    if mm == 2 and dd < 1 or dd > 29:
        return False
    
    # If the date is in months 1, 3, 5, 7, 8, 10, 12, the day is valid if it's between 1 and 31