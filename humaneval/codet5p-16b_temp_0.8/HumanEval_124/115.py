
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
    else:
        dates = date.split('-')
        if int(dates[0]) > 12 or int(dates[0]) < 1:
            return False
        elif int(dates[2][2:]) < 1 or int(dates[2][2:]) > 12:
            return False
        elif int(dates[1]) > 31 or int(dates[1]) < 1:
            if int(dates[0]) == 2:
                if int(dates[1]) > 29:
                    return False
            elif int(dates[0]) in [1, 3, 5, 7, 8, 10, 12]:
                if int(dates[1]) > 30:
                    return False
            elif int(dates[0]) in [4, 6, 9, 11]:
                if int(dates[1]) > 31:
                    return False
            else:
                return False
        elif int(dates[1]) > 12 or int(dates[1]) < 1:
            return False
        else:
            return True
