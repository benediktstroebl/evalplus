import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r"^(\d{2})-(\d{1,2})-(\d{4})$", date)
    
    if not date_parts or date_parts.group(3) == '':
        return False
    
    year = int(date_parts.group(3))
    month = int(date_parts.group(2))
    day = int(date_parts.group(1))
    
    # Check if the date is valid
    if 1 <= month <= 12:
        if (month == 2 and day != 29) or (month != 2 and (day < 1 or day > 31)):
            return False
    else:
        return False
    
    if not 1 <= day <= 31:
        return False
    
    if not 2000 <= year <= 2030:
        return False
    
    return True