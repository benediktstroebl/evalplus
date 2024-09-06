import re
def valid_date(date):
    """
    Validate a given date string and return True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if ((dd<1 or dd>31) and (mm in [1, 3, 5, 7, 8, 10, 12])) or (dd<1 or dd>30 and mm in [4, 6, 9, 11]) or (dd<1 or dd>29 and mm==2):
        return False
    
    # Year and day of the week checks
    if mm<1 or mm>12 or dd<1 or dd>31:
        return False
    
    return True