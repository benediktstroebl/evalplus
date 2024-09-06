import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Month and Day validation
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or dd > diary_days[mm]:
        return False

    # Year Validation
    if yyyy < 1000 or yyyy > datetime.datetime.now().year + 1:
        return False

    return True
def diary_days(month):
    """
    Returns the number of days in a month for given month parameter
    """
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    return days[month - 1] if 1 <= month <= 12 else 0