import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.strip()
        mm, dd, yyyy = map(int, date.split('-'))
    except ValueError:
        return False

    # Month validation
    if 1 <= mm <= 12:
        if (mm == 2 and dd >= 1 and dd <= 29) or (mm not in [2,4,6,9,11] and dd >= 1 and dd <= 31) or mm in [1,3,5,7,8,10,12]:
            return True
        else:
            return False
    else:
        return False

    # Year validation
    if 1900 <= yyyy <= 2023:
        return True
    else:
        return False