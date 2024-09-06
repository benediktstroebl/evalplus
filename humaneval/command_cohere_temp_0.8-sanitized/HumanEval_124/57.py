import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.findall(r'(\d{2})[-/\s](\d{1,2})[-/\s](\d{4})', date))
    
    # Checks for constraints on month and day
    if (
        (dd<1 or dd>31) if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12) else
        (dd<1 or dd>30) if (mm==4 or mm==6 or mm==9 or mm==11) else
        (dd<1 or dd>29) if mm==2 else True
    ):
        return False
    
    # Check for constraint on year
    if yyyy<1000 or yyyy>9999:
        return False
    
    # Check for valid date format
    if not re.match(r'^(\d{2})[-/\s](\d{1,2})[-/\s](\d{4})$', date):
        return False
    
    return True