import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d\d\d\d)", date).groups())
    
    # Month and day validation
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or dd > diary_days[mm]:
        return False
    
    # Check date format
    date_format = f"%d-%m-%Y"
    if date.format != date_format:
        return False
    
    return True
diary_days = {
    1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
    4: 30, 6: 30, 9: 30, 11: 30,
    2: 29,
}