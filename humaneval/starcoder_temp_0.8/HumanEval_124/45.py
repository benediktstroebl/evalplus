
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
    
    if len(date) < 10:
        return False
    
    try:
        date_comps = date.split('-')
        month = int(date_comps[0])
        day = int(date_comps[1])
        year = int(date_comps[2])
    except:
        return False
    
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day < 1 or day > 31:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                return False
        elif month == 2:
            if year % 4 == 0 and year % 100!= 0:
                if day < 1 or day > 29:
                    return False
            elif year % 400 == 0:
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
    return True
