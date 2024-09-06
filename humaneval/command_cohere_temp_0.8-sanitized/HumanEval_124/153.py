import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_components = re.match(r'(\d{2})[-/](\d{1,2})[-/](\d{4})', date)
    
    if not date_components or date_components.groups() != 3:
        return False
    
    year, month, day = map(int, date_components.groups())
    
    # Validate year, month, and day
    if 1 <= year < 1000 or year > 9999:
        return False
    
    if not (1 <= month <= 12):
        return False
    
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2:
        if day < 1 or day > 29:
            return False
    else:
        if day < 1 or day > month_days[month - 1]:
            return False
    
    return True