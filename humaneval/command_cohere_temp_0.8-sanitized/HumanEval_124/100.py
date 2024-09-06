import re
def valid_date(date):
    """
    Validate a given date string and return True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    yyyy, mm, dd = map(int, re.sub(r'[^0-9]', '', date).split('-'))
    
    # Check if the date is valid
    if (mm < 1 or mm > 12) or (dd < 1 or dd > dias_anos[mm] ) or (yyyy < 2000):
        return False
    
    return True
dias_anos = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}