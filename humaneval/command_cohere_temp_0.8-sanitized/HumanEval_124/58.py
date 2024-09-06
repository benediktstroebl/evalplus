import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d\d\d\d)', date).groups())

    # Month checks
    if (dd < 1 or dd > 31) and (dd < 1 or dd > 30) and (dd < 1 or dd > 29):
        return False

    # Year check
    if mm < 1 or mm > 12 or dd < 1 or dd > days_in_month(mm, yyyy):
        return False

    return True
def days_in_month(month, year):
    days_in_month_1_to_12 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month_1_to_12[month - 1]