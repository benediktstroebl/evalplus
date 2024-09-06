import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)[-/](\d?\d?)[-/](\d{4})$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Month ranges
    if month <= 0 or month > 12:
        return False
    if month == 2 and day > 29:
        return False
    max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= month <= 3 and day < 1 or day > max_day[month - 1]:
        return False
    if 4 <= month <= 6 and day < 1 or day > max_day[month - 1]:
        return False
    if 7 <= month <= 9 and day < 1 or day > max_day[month - 1]:
        return False
    if 10 <= month <= 12 and day < 1 or day > max_day[month - 1]:
        return False

    return True