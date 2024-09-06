import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r"^(\d{2})[-/](\d{1,2})[-/](\d{4})$", date)
    
    if not date_parts or date_parts.group(3) == "0000":
        return False
    
    year = int(date_parts.group(3))
    month = int(date_parts.group(2))
    day = int(date_parts.group(1))
    
    # Month and day validation
    if 1 <= month <= 12:
        month = [1, 3, 5, 7, 8, 10, 12].index(month) + 1
        max_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30][month - 1]
        if day < 1 or day > max_day:
            return False
    
    # Date format validation
    if not re.match(r"^(\d{2})[-/](\d{1,2})[-/](\d{4})$", date):
        return False
    
    # Month validation
    if 1 <= month <= 12:
        return True
    
    return False