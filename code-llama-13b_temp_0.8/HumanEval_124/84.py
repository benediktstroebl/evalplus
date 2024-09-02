
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
    month = {
        1 : 31,
        2 : 29,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    if date == '':
        return False
    
    date_splited = date.split('-')
    if len(date_splited) != 3:
        return False
    
    month_number = int(date_splited[0])
    day_number = int(date_splited[1])
    year = int(date_splited[2])
    
    if month_number > 12 or month_number < 1:
        return False
    
    if month_number in [1,3,5,7,8,10,12]:
        if day_number > 31 or day_number < 1:
            return False
    elif month_number in [4,6,9,11]:
        if day_number > 30 or day_number < 1:
            return False
    elif month_number == 2:
        if year % 4 == 0 and year % 100 != 0:
            if day_number > 29 or day_number < 1:
                return False
        else:
            if day_number > 28 or day_number < 1:
                return False
    
    return True

