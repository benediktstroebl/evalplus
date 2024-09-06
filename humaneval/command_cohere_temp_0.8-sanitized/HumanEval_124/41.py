import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.strip()
        date = date.replace('/', '-')
        date = re.sub('[^0-9]', '', date)
        year, month, day = map(int, date.split('-'))
    except ValueError:
        return False

    if 1 <= month <= 12:
        if (month, day) in [(1, 31), (3, 31), (5, 31), (7, 31), (8, 31), (10, 31), (12, 31)]:
            return True
        elif (month, day) in [(4, 30), (6, 30), (9, 30), (11, 30)]:
            return day <= 30
        elif month == 2 and 1 <= day <= 29:
            return True
    return False