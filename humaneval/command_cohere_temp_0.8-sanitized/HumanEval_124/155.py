import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month checks
    if (mm < 1 or mm > 12) or (dd < 1 or dd > diary_days(mm)):
        return False
    
    # Year checks
    if yyyy < 1000 or yyyy > 2030: 
        return False
    
    return True
def diary_days(month):
    # Returns the number of days in a month for given year
    if (month == 2): 
        return 29  
    elif (month == 4 or month == 6 or month == 9 or month == 11): 
        return 30 
    else: 
        return 31
date = '06-04-2020'