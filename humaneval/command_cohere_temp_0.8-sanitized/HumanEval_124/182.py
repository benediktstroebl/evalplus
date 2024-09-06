import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Validate day and month
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or (mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd > 30) or (mm != 2 and mm != 4 and mm != 6 and mm != 9 and mm != 11 and dd > 31):
        return False
    
    # Validate year
    if yyyy < 1900 or yyyy > 2050:  # This is somewhat arbitrary, depending on what years you want to consider valid
        return False
    
    return True