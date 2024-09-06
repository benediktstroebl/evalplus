import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())
    
    # Month range validation
    if (dd < 1 or dd > lenient_day_range(mm)) or mm < 1 or mm > 12:
        return False

    # Date format validation
    if re.match(r'^(\d\d)-(\d\d)-(\d\d\d\d)$', date):
        return True
    else:
        return False
def lenient_day_range(month):
    """
    Returns the range of days for a given month, with special cases for February.
    """
    if month == 2:
        return [1, 29]
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return [1, 31]
    elif month in [4, 6, 9, 11]:
        return [1, 30]
    else:
        return None