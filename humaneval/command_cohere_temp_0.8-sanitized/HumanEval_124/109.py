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
    
    year, month, day = map(int, date_parts.groups())
    
    # Check if the date is within valid range