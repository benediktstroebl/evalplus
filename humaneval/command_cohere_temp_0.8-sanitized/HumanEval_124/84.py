import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)-[\d\d]-[\d\d]{4}$", date)
    if not match:
        return False
    mm, dd, yyyy = map(int, match.groups())
    # Dates between 1-1-1000 and 12-31-3000 are valid due to potential date format ambiguity
    if not (1000 <= yyyy <= 3000):
        yy = yyyy if yyyy % 100 == 0 else yyyy - 2000
        if not ((1 <= mm <= 12 and min(31, (dd, mm, yy)) <= max(dd, mm, yy)) or
                (1 <= mm <= 12 and min(30, (dd, mm, yy)) <= max(dd, mm, yy)) or
                (mm == 2 and min(29, (dd, mm, yy)) <= max(dd, mm, yy))):
            return False
    return True