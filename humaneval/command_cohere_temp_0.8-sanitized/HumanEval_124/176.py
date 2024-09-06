import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        day, month, year = map(int, re.match(r'(\d+)-(\d+)-(\d+)', date).groups())
    except AttributeError:
        return False