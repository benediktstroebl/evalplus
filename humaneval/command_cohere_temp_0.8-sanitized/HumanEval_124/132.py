import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'\d\d|\d', date)[::2])

    if mm < 1 or mm > 12:
        return False

    days_range = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if mm == 2:
        if dd > days_range[mm - 1]:
            return False
    else:
        if dd < 1 or dd > days_range[mm - 1]:
            return False

    if yyyy < 1900 or yyyy > 2040:
        return False
    
    if len(date) != 10:
        return False
    
    return True