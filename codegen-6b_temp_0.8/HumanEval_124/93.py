
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
    try:
        if len(date) == 0:
            return False
        f_date = date.split('-')
        f_months = [1,3,5,7,8,10,12]
        date_months = [4,6,9,11]
        date_days = [2,29,30,31]
        if len(f_date) != 3:
            return False
        if int(f_date[0]) not in f_months or int(f_date[1]) not in date_days or int(f_date[2]) < 1:
            return False
        if int(f_date[0]) in f_months and int(f_date[1]) not in date_days:
            return False
        if int(f_date[0]) in f_months and int(f_date[1]) not in date_days and int(f_date[2]) < 1:
            return False
        if int(f_date[0]) not in f_months and int(f_date[1]) not in date_days and int(f_date[2]) < 1:
            return False
        if int(f_date[1]) not in date_days:
            return False
        if int(f_date[2]) < 1:
            return False
        return True
    except ValueError:
        return False
