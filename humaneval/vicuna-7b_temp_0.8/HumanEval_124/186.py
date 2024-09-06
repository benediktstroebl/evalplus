
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
    # check if the date string is not empty
    if len(date) == 0:
        return False
    
    # check if the number of days is valid
    if int(date[-2]) < 1 or int(date[-2]) > 31 or int(date[-1]) < int(date[-2]) or int(date[-1]) > 31:
        return False
    
    # check if the month is valid
    if int(date[-1]) < 1 or int(date[-1]) > 12:
        return False
    
    # check if the date is in the correct format
    if date[-1] < 10:
        day = int(date[-2])
        month = int(date[-1])
        year = int(date[0..2])
        if (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1 or year > 2020):
            return False
    else:
        day = int(date[-2])
        month = int(date[-5..-3])
        year = int(date[0..2])
        if (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1900 or year > 2038):
            return False
    return True
