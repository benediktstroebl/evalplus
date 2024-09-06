def valid_date(date):
    """
    Validates a date string and returns True if valid, False otherwise.

    Args:
        date (str): Date string in the format "mm-dd-yyyy"

    Returns:
        bool: True if the date string is valid, False otherwise
    """
    import re

    date = date.strip()  # Remove leading and trailing spaces
    date = date.replace('/', '-')  # Convert '/' to '-'
    if not re.match(r"^[0-9]{2}-[0-9]{2}-[0-9]{4}$", date):
        return False

    year, month, day = map(int, date.split('-'))

    if 1 <= month <= 12:
        if month == 2 and day != 29:
            return False
        if month == 4 or month == 6 or month == 9 or month == 11 and day not in range(1, 31):
            return False
        if month != 2 and day not in range(1, 32):
            return False
    else:
        return False

    return True