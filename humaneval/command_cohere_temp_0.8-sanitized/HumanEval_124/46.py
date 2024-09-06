import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        date = date.strip()
        date = date.split('-')
        mm = int(date[0])-1
        dd = int(date[1])
        yyyy = int(date[2])
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 29, 31, 30, 31]

        if mm < 0 or mm > 11 or dd < 0 or dd > days_in_month[mm] or yyyy < 1000 or yyyy > 3000:
            return False
        return True
    except:
        return False