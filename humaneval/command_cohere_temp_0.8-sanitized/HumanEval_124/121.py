def valid_date(date):
    """Validate a date string and return True if valid, otherwise False."""
    import re

    DATE_PATTERN = r"^(\d\d?)[-/](\d\d?)[-/](\d{4})$"

    if not re.match(DATE_PATTERN, date):
        return False

    year, month, day = map(int, date.split('-'))

    if 1 <= month <= 12:
        if month == 2 and day != 29:
            return False
        if month == 4 or month == 6 or month == 9 or month == 11 and day not in range(1, 31):
            return False
        if 1 <= month <= 3 or 5 <= month <= 8 or 10 <= month <= 12 and day not in range(1, 32):
            return False
    else:
        return False

    return True