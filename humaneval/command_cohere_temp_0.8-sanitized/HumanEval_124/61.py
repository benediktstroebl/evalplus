import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/\s](\d{2})[-/\s](\d{4})', date))
    
    # Checks for the number of days and months
    if (
            (dd < 1 or dd > 31) and 
            (dd < 1 or dd > 30) and 
            (dd < 1 or dd > 29)
      ):
        return False
    
    if (
            (mm < 1 or mm > 12)
      ):
        return False
    
    # Checks for the date format
    if re.search(r'^(\d{2})[-/\s](\d{2})[-/\s](\d{4})$', date) is None:
        return False

    return True