
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
    valid = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    valid[0] = True
    valid[1] = True
    valid[2] = True
    valid[3] = True
    valid[4] = True
    valid[5] = True
    valid[6] = True
    valid[7] = True
    valid[8] = True
    valid[9] = True
    valid[10] = True
    valid[11] = True
    valid[12] = True

    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:10])

    # 01-01-1900
    if year < 1900:
        return False

    # 01-01-2000
    if valid[month] == False:
        valid[month] = True
    elif valid[month] == True:
        if valid[day] == False:
            valid[day] = True
        elif valid[day] == True:
            if valid[year] == False:
                valid[year] = True
            elif valid[year] == True:
                return True
    return False

