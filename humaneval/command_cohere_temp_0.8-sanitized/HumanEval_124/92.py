import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    
    # Extract year, month, and day from the date string
    date_components = re.match(r"^(\d{2})-(\d{1,2})-(\d{4})$", date)
    
    if not date_components or date_components.group(3) == "0000":
        return False
    
    year = date_components.group(3)
    month = date_components.group(2)
    day = date_components.group(1)
    
    # Validate day, month, and year
    if '01' <= day <= '31' and month in ['1', '3', '5', '7', '8', '10', '12'] \
       or '01' <= day <= '30' and month in ['4', '6', '9', '11'] \
       or '01' <= day <= '29' and month == '2':
        return True
    
    return False