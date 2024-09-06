import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if ((dd<1 or dd>31) and (mm in [1,3,5,7,8,10,12])) or ((dd<1 or dd>30) and (mm in [4,6,9,11])) or (dd<1 or dd>29 and mm==2):
        return False
    
    # Year and day order checks
    if not (1000<=yyyy<=9999 and mm<=12 and dd<=31):
        return False
    
    return True