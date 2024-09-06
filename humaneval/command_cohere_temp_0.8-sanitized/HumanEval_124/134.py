import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False

    # Extract year, month, and day from the date string
    date_parts = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)

    if not date_parts:
        return False

    year, month, day = date_parts.groups()

    # Check if the date is valid
    if not (1 <= int(month) <= 12 and
                1 <= int(day) <= np_days[month - 1] and
                2000 <= int(year) <= 2030):
        return False

    return True
np_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}