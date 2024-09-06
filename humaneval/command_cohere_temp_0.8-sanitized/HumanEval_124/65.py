import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d|\d', date))
    
    if mm < 1 or mm > 12:
        return False
    
    # Determine number of days based on month
    if (mm == 2 and dd != 29) or (mm in [1, 3, 5, 7, 8, 10, 12] and dd < 1 or dd > 31) or (mm in [4, 6, 9, 11] and dd < 1 or dd > 30):
        return False
    
    # Validate year
    if yyyy < 1900 or yyyy > 2030:
        return False
    
    # Validate date format
    if date.split('-')[0].split('/')[0] != str(mm):
        return False
    if date.split('-')[1].split('/')[0] != str(dd):
        return False
    if date.split('-')[2].split('/')[0] != str(yyyy):
        return False
    
    return True