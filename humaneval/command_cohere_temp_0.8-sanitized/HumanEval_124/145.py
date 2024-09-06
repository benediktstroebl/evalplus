import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())
    
    # Month range validation
    if (dd < 1 or dd > lenient_day_range(mm)) or mm < 1 or mm > 12:
        return False
    
    # Date format validation
    if not re.match(r'^(\d\d)-(\d\d)-(\d{4})$', date):
        return False
    
    return True
def lenient_day_range(month):
    """
    Returns the valid range of days for a given month.
    Months 1, 3, 5, 7, 8, 10, and 12 return 31, 30 days respectively.
    Months 4, 6, 9, and 11 return 30 days.
    Month 2 returns 29 days.
    """
    if (month > 0 and month < 7) or (month > 6 and month < 11) or month == 2:
        return 31 if month == 2 else 30
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31