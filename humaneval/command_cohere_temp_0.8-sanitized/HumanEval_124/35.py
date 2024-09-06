import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_parts = re.match(r'(\d{2})-(\d{1,2})-(\d{4})', date)
    
    if not date_parts:
        return False
    
    year, month, day = date_parts.groups()
    
    # Validate day value
    if 1 <= int(day) <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= int(day) <= 31
        elif month in [4, 6, 9, 11]:
            return 1 <= int(day) <= 30
        elif month == 2:
            return 1 <= int(day) <= 29
        else:
            return False
    else:
        return False
    
    # Validate month value
    if 1 <= int(month) <= 12:
        return True
    else:
        return False
    
    # Validate year value
    date_parts = re.match(r'(\d{2})-(\d{1,2})-(\d{4})', date)
    
    if not date_parts:
        return False
    
    year, month, day = date_parts.groups()
    
    return 2000 <= int(year) <= 2030