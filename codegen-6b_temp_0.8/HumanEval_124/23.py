
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
        if date.strip() == '':
            return False
        elif date[1] == '-' and date[3] == '-':
            n_days = int(date[0] + date[1] + date[2] + date[3])
            n_days2 = int(date[5] + date[6] + date[7] + date[8])
            month = int(date[4])
            if n_days > 31 or (month > 12 or month < 1):
                return False
            elif n_days2 > 29 or (month == 2 and n_days2 > 28):
                return False
            elif n_days2 == 29 and month not in [4, 6, 9, 11]:
                return False
            else:
                return True
        else:
            return False
    except:
        return False
