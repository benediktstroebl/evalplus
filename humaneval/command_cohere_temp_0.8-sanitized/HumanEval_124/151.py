import re
def valid_date(date):
    """
    Validate a date string and return True if the date is valid.
    
    Args:
        date (str): A date string in the format "mm-dd-yyyy".
    
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    if not date:
        return False
    
    mm, dd, yyyy = map(int, re.match(r"(\d\d)-(\d\d)-(\d{4})", date).groups())
    
    # Check if the day and month values are within the valid range
    if mm < 1 or mm > 12 or dd < 1 or ((mm <= 2 and dd > 29) or (mm > 2 and dd > 31)):
        return False
    
    # Check if the year value is four digits only
    if len(yyyy) != 4:
        return False
    
    return True