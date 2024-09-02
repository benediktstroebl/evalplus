
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
    
    if len(date) == 0:
        return False
    
    days_months = [1,3,5,7,8,10,12]
    days = ['01','03','05','07','08','10','12']
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    
    if date[2] != '-' or date[5] != '-':
        return False
    
    for digit in date:
        if digit == '-':
            pass
        else:
            if digit not in months and digit not in days:
                return False
    
    if date[0:2] not in months or date[3:5] not in days or date[6:] not in months:
        return False
    
    if date[3:5] == '02':
        if date[0:2] == '02':
            return False
        elif int(date[6:]) % 4 == 0:
            if int(date[3:5]) > 29:
                return False
        elif int(date[3:5]) > 28:
            return False
    else:
        if date[0:2] in days_months:
            if int(date[3:5]) > 31:
                return False
        elif int(date[3:5]) > 30:
            return False
    return True

    
