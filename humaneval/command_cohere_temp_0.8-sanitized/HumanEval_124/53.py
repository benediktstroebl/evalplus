import re
def valid_date(date):
    """
    Validate a date string and returns True if date is valid otherwise False .
    """
    date = date.strip()
    if not date:
        return False
    match = re.match(r"^(\d{1,2})[-/](\d{1,2})[-/](\d{4})$", date)
    if not match:
        return False
    mm, dd, yyyy = map(int, match.groups())

    # Days must be between 1 and the last day of the month.
    last_day = datetime.date(yyyy, mm, 1).isocalendar()[1]
    if 1 <= dd <= last_day:
        return True
    else:
        return False