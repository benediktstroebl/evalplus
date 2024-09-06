
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
    import re

    date_valid = re.compile(r'\d{2}-\d{2}-\d{4}')
    date = date.replace('-', ' ').split()
    if len(date) == 3 and date_valid.match(date[2]):
        if date[0] == '01' or date[0] == '03' or date[0] == '05' or date[0] == '07' or date[0] == '08' or date[
            0] == '10' or date[0] == '12':
            if 1 <= int(date[1]) <= 31:
                return True
            elif int(date[1]) < 1:
                return False
        elif date[0] == '04' or date[0] == '06' or date[0] == '09' or date[0] == '11':
            if 1 <= int(date[1]) <= 30:
                return True
            elif int(date[1]) < 1:
                return False
        elif date[0] == '02':
            if 1 <= int(date[1]) <= 29:
                return True
            elif int(date[1]) < 1:
                return False
        else:
            return False
    return False

