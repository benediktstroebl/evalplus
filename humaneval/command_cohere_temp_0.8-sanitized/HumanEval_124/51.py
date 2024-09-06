import re
def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    """
    if not date:
        return False

    # Check date format: mm-dd-yyyy
    match = re.match(r"^(\d{2})-(\d{2})-(\d{4})$", date)
    if not match:
        return False

    day, month, year = map(int, match.groups())

    # Check day validity
    if 1 <= month <= 12:
        if 1 < day < days_in_month(month):
            return True
        else:
            return False
    else:
        return False

    return True
def days_in_month(month):
    # Number of days in each month
    months_days = [
        31,   # January
        29,   # February (leap year)
        31,   # March
        30,   # April
        31,   # May
        30,   # June
        31,   # July
        31,   # August
        30,   # September
        31,   # October
        30,   # November
        31,   # December
    ]
    if 1 <= month <= 12:
        return months_days[month - 1]
    else:
        return 0