import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if (dd<1 or dd>31) and (dd<1 or dd>30) and (dd<1 or dd>29):
        return False
    
    # Year and day of the week checks
    if mm<1 or mm>12 or dd<1 or dd>days_in_month[mm-1]:
        return False
    
    return True
def days_in_month():
    return [31, 29, 29, 30, 30, 31, 31, 30, 30, 31, 31]