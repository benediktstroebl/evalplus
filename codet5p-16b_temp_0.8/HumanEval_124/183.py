
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
        date = date.split('-')
        month, day, year = int(date[0]), int(date[1]), int(date[2])
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_with_30_days = [4, 6, 9, 11]
        months_with_29_days = [2]
        if 0 < month < 13:
            if month in months_with_31_days:
                if 1 <= day <= 31:
                    return True
            elif month in months_with_30_days:
                if 1 <= day <= 30:
                    return True
            elif month in months_with_29_days:
                if 1 <= day <= 29:
                    return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False
    except IndexError:
        return False
    else:
        return False

    
