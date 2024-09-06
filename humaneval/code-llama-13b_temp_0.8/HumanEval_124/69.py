
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    
    #check for empty string
    if date == "":
        return False
    
    #check for the date format
    try:
        date = date.split("-")
        d = int(date[1])
        m = int(date[0])
        y = int(date[2])
    except:
        return False
    
    #check for days
    if m in [1,3,5,7,8,10,12]:
        if d > 0 and d <= 31:
            pass
        else:
            return False
    elif m in [4,6,9,11]:
        if d > 0 and d <= 30:
            pass
        else:
            return False
    elif m == 2:
        if d > 0 and d <= 29:
            pass
        else:
            return False
    else:
        return False
    
    #check for months
    if m > 0 and m <= 12:
        pass
    else:
        return False
    
    return True
