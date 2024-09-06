import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/](\d{2})[-/](\d{4})', date))
    
    # Checks for the number of days and months
    if (
        (dd<1 or dd>31) and 
        (dd<1 or dd>30) and 
        (dd<1 or dd>29)
        ):
        return False
    
    if mm<1 or mm>12:
        return False
    
    # Check date format
    if date.split('-').count(date[0]) != 3:
        return False
    
    return True