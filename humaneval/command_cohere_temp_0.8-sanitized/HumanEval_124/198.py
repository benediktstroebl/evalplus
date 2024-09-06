import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d|\d', date))
    
    # Checks for the date format and separates month, day, year
    if len(date.split('-')!= 3 or not all(c in '-' for c in date)):
        return False
    
    # Checks for month being in the range 1-12
    if (mm < 1 or mm > 12):
        return False
    
    # Depending on the month, checks for the day being in the range 1-31 or 1-30
    # Days can be 31 in months 1, 3, 5, 7, 8, 10, 12 but not in month 4, 6, 9, 11
    # Days can be 30 in month 2 but not in month 4
    if (dd < 1 or (dd not in [30, 31] and mm not in [2, 4]) or dd > (mm == 4 and dd != 30 + 1) + 30):
        return False
    
    # Checks for the year being in the range 2000-2099
    if yyyy < 2000 or yyyy > 2020:
        return False
    
    return True