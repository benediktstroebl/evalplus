import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    try:
        year, month, day = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
        if (month < 1 or month > 12) or (day < 1 or day > DAY_DICT[month]):
            return False
        if not (2000 <= year <= 2020):
            return False
    except:
        return False
    return True
DAY_DICT = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}