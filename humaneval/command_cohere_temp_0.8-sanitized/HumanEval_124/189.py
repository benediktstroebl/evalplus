import re
def valid_date(date):
    """
    Validate a date string and returns True if the date is valid otherwise False
    """
    if not date:
        return False
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if match:
        mm, dd, yyyy = map(int, match.groups())
        if 1 <= mm <= 12:
            if (dd <= maxdays[mm - 1] and dd > 0) or mm == 2:
                return True
        return False
    else:
        return False
maxdays = {
    1: 31, 3: 31, 5: 31, 7: 31, 
    8: 31, 10: 31, 12: 31, 
    4: 30, 6: 30, 9: 30, 11: 30, 
    2: 29
}