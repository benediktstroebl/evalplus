import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/\s](\d{2})[-/\s](\d{4})', date))
    
    # Month range validation
    if (mm < 1 or mm > 12) or (
           mm == 2 and dd not in range(1, 32) or 
           mm == 4 or mm == 6 or mm == 9 or mm == 11 and dd not in range(1, 31) or 
           mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12 and dd not in range(1, 31)
        ):
        return False
    
    # Year validation
    if yyyy < 1900 or yyyy > 2050:
        return False
    
    # Day validation
    if dd < 1 or dd > 31:
        return False
    
    # Format validation
    date_format = re.compile(r"^(\d{2})[-/\s](\d{2})[-/\s](\d{4})$")
    if not date_format.match(date):
        return False
    
    return True