import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.match(r'(\d{4})-(\d{2})-(\d{2})', date).groups())
    
    # Check if the date is in the correct format
    if not re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date):
        return False
    
    # Check if the day value is valid for the specific month
    days_valid_for_month = [None, 31, 29, 31, 30, 31, 30, 31, 29, 31]