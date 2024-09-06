
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
    
    # Check that date is not empty 
    if date == '':
        return False

    # Check that date is in the format: mm-dd-yyyy
    if date.count('-') != 2:
        return False

    months = [1,3,5,7,8,10,12]
    for month in months:
        if int(date[:2]) == month and 1 <= int(date[3:5]) <= 31:
            break
        else:
            return False

    months = [4,6,9,11]
    for month in months:
        if int(date[:2]) == month and 1 <= int(date[3:5]) <= 30:
            break
        else:
            return False

    if int(date[:2]) == 2 and 1 <= int(date[3:5]) <= 29:
        pass
    else:
        return False

    if 1 <= int(date[3:5]) <= 12:
        pass
    else:
        return False

    return True
