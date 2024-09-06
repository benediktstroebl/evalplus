import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Check day validity
    day_valid = (dd >= 1 and dd <= 31) if (mm == 2 or (mm > 2 and mm % 2 == 0)) else (dd >= 1 and dd <= 30)
    
    # Check month validity
    month_valid = (mm >= 1 and mm <= 12)
    
    return day_valid and month_valid and date_format_valid
def date_format_valid():
    return re.match(r'^(\d\d)-(\d\d)-(\d{4})$', date).group() == date