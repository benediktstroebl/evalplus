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
        mm, dd, yyyy = map(int, date)

        if 1 <= mm <= 12:
            max_days = 30 if (mm == 4 or mm == 6 or mm == 9 or mm == 11) else 31
            if dd < 1 or dd > max_days:
                return False
        else:
            return False

        if 1970 <= yyyy <= 2030:
            if not re.match(r"^[0-9]{4}$", str(yyyy)):
                return False
        else:
            return False

        return True
    except Exception:
        return False