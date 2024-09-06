import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.split('-')
        m = int(date[0]) - 1
        d = int(date[1])
        y = int(date[2])
        if m < 0 or m > 11 or d < 1 or d > LEAP(y, m) or not re.match(r'^[0-9]{2}-[0-9]{2}-[1-9]\d{3}$', date[0:] + date[2:]):
            return False
        return True
    except:
        return False
def LEAP(y, m):
    # Leap year calculation
    if (y % 4 == 0 and m <= 2) or y % 400 == 0:
        return 31
    elif m == 2:
        return 29
    else:
        return 30