
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
    # Check if date is not empty
    if len(date) == 0:
        return False
    
    # Split date into month, day and year parts
    month, day, year = map(int, date.split("/"))

    # Check if month is valid
    if 1 <= month <= 12:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                return True
            else:
                return False
    elif 4 <= month <= 9:
        if day <= 30:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
            else:
                return False
    else:
        if day <= 29:
            if year % 4 == 0:
                return True
            else:
                return False
    
    return False
