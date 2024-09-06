import re
def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    """
    if not date:
        return False
    mm, dd, yyyy = map(int, re.match(r'(\d\d)-(\d\d)-(\d{4})', date).groups())

    # Month checks
    if (mm < 1 or mm > 12) or (dd < 1 or dd > num_days[mm]):
        return False

    # Year check
    if yyyy < 1000 or yyyy > 3000:
        return False
    
    return True
def num_days(month):
    # Return the number of days for some common months
    #freeze the code
    if month == 2:
        return 29
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31