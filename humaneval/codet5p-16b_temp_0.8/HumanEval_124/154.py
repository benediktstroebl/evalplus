
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
        l = date.split('-')
        if len(l)!= 3:
            return False
        else:
            try:
                if (int(l[1]) > 12) or (int(l[1]) < 1):
                    return False
                elif (int(l[0]) > 12) or (int(l[0]) < 1):
                    return False
                elif (int(l[2]) > 2020) or (int(l[2]) < 2000):
                    return False
                elif (int(l[0]) in (4, 6, 9, 11) and int(l[1]) in (1, 3, 5, 7, 8, 10, 12)) and (int(l[2]) < 1):
                    return False
                elif (int(l[0]) == 2) and (int(l[1]) in (4, 6, 9, 11) and int(l[2]) < 1):
                    return False
                elif (int(l[0]) in (1, 3, 5,
