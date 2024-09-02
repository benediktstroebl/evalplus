
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
    if date == '':
        return False

    months_with_30 = [4, 6, 9, 11]
    months_with_31 = [1, 3, 5, 7, 8, 10, 12]
    months_with_29 = [2]
    months_with_28 = [13]
    days = ['31', '30', '29', '28']
    months = ['12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
    
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month = date_parts[0]
    day = date_parts[1]
    year = date_parts[2]
    
    if month not in months:
        return False
    
    if day not in days:
        return False

    if month in months_with_30:
        if day == '31':
            return False
    
    if month in months_with_31:
        if day == '32':
            return False

    if month in months_with_29:
        if day == '30':
            return False

    if month in months_with_28:
        if day == '29':
            return False
    
    return True
