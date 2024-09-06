def valid_date(date):
    """
    Validate a date string and return True if valid, otherwise False.
    A date is valid if:
    1. Date string is not empty.
    2. Number of days is valid:
        - Between 1 and 31 for months 1, 3, 5, 7, 8, 10, 12.
        - Between 1 and 30 for months 4, 6, 9, 11.
        - Between 1 and 29 for month 2 (feb).
    3. Month is between 1 and 12.
    4. Date string is in the format: mm-dd-yyyy.
    """
    if not date:
        return False
    day, month, year = map(int, date.split('-'))
    if 1 <= month <= 12:
        if (month == 2 and day <= 29) or (month != 2 and day <= 31):
            return True
        else:
            return False
    else:
        return False