
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
        # '09-25-2021'
        # '09-25-2021'
        mm, dd, yyyy = date.split("-")
    except:
        return False

    try:
        # 2021
        # 2021
        yyyy = int(yyyy)
        # 09
        # 09
        mm = int(mm)
        # 25
        # 25
        dd = int(dd)

        if yyyy < 1:
            return False
        if yyyy > 2031:
            return False
        if mm < 1:
            return False
        if mm > 12:
            return False
        if dd < 1:
            return False
        if dd > 31:
            return False
        if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
            if dd > 31:
                return False
        if mm == 4 or mm == 6 or mm == 9 or mm == 11:
            if dd > 30:
                return False
        if mm == 2:
            if yyyy % 4 == 0 and (yyy % 100 != 0 or yyy % 400 == 0):
                if dd > 29:
                    return False
            else:
                if dd > 28:
                    return False
        return True
    except:
        return False
