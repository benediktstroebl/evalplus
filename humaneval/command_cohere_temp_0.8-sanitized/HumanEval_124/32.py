import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)[-/](\d?\d?)[-/](\d\d)\D*$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Month ranges
    if (month <= 0 or month > 12) or (month == 2 and day > 29) or (month == 4 or month == 6 or month == 9 or month == 11 and day > 30):
        return False
    
    # Year range
    if year < 1000 or year > datetime.datetime.now().year:
        return False
    
    return True