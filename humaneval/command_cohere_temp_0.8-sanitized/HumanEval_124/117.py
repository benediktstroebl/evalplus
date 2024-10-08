import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Month checks
    if (mm < 1 or mm > 12) or (
           (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30) or (
           mm == 2 and dd > 29):
        return False

    # Day checks
    if dd < 1 or mm == 2 and dd > 29 or (mm != 2, 4, 6, 9, 11) and dd > 31:
        return False

    # Format check
    if not re.match(r'^(\d\d)-(\d\d)-(\d{4})$'.format(mm, dd, yyyy), date):
        return False

    return True