import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())

    # Month checks
    if (mm < 1 or mm > 12) or ((mm == 2) and (dd < 1 or dd > 29)) or ((mm < 4 or mm > 6) and (dd < 1 or dd > 30)):
        return False

    # Day check
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30):
        return False

    # Format check
    if not re.match(r'^(\d\d)-(\d\d)-(\d{4})$', date):
        return False

    return True