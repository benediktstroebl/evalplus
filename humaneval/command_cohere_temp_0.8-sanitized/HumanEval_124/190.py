import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.sub(r'[^0-9]', '', date).split('-'))
    
    # Check if the date is in the correct format (mm-dd-yyyy)
    if not re.match(r'^(\d{1,2})-(\d{1,2})-(\d{4})$', date):
        return False
    
    # Check if the day is valid for the specific month
    days_valid_for_month = [31, 30, 31, 30, 31, 30, 31, 30, 31]
    if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
        if 1 <= dd <= days_valid_for_month[mm - 1]:
            return True
        else:
            return False
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if 1 <= dd <= days_valid_for_month[mm - 1]:
            return True
        else:
            return False
    elif mm == 2:
        if 1 <= dd <= 29:  # Allow for leap years
            return True
        else:
            return False
    
    # Check if the month is valid (1-12)
    if 1 <= mm <= 12:
        return True
    else:
        return False