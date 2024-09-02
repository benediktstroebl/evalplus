
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
    months = ["1", "3", "5", "7", "8", "10", "12"]
    days = [31, 30, 29, 28, 31, 30, 31, 31, 30, 31, 30, 31]
    
    months_int = [31,28,31,30,31,30,31,31,30,31,30,31]
    days_int = [31,30,31,30,31,30,31,31,30,31,30,31]

    date_split = date.split("-")
    if len(date_split) != 3:
        return False
    
    try:
        month = int(date_split[0])
        day = int(date_split[1])
    except ValueError:
        return False
    
    if (month <= 0 or month > 12) or (day <= 0 or day > months_int[month-1]):
        return False
    
    year = int(date_split[2])

    if (month == 2) and (day > 29) or (month == 4) and (day > days_int[month-1]) or (month == 6) and (day > 31) or (month == 9) and (day > 30) or (month == 11) and (day > 31) or (month == 12) and (day > 31):
        return False

    return True
