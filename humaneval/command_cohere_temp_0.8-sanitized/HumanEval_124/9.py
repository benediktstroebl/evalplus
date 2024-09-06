import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())

    # Month checks
    if (dd<1) or (dd>=(30 if (mm==2) else 31)):
        return False

    # Year check
    if yyyy<1000 or yyyy>2030:
        return False

    return True