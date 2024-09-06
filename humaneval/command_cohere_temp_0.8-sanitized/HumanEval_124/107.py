import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    match = re.match(r"^(\d?\d?)[-/](\d?\d?)[-/](\d{4})$", date)
    if not match:
        return False
    day, month, year = map(int, match.groups())
    
    # Month ranges
    month_ranges = [(1, 31), (3, 31), (5, 31), (7, 31),
                    (8, 31), (10, 31), (12, 31),
                    (4, 30), (6, 30), (9, 30), (11, 30), (2, 29)]
    for m_min, m_max in month_ranges:
        if month < m_min or month > m_max:
            return False
    
    # Day ranges
    if month == 2:
        if day < 1 or day > 29:
            return False
    else:
        if day < 1 or day > 31:
            return False
    
    return True