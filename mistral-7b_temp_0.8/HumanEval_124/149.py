
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
            raise ValueError
        else:
            date = date.split('-')
            if int(date[2]) > 0 and len(date[2]) == 4:
                if int(date[0]) > 0 and int(date[0]) <= 12:
                    if int(date[1]) > 0 and int(date[1]) <= 31:
                        if int(date[1]) == 1:
                            if int(date[2])%4 == 0 and len(str(date[2]) == 4):
                                if int(date[1]) > 0 and int(date[1]) <= 29:
                                    return True
                                else:
                                    return False
                            else:
                                if int(date[1]) > 0 and int(date[1]) <= 28:
                                    return True
                                else:
                                    return False
                        elif int(date[1]) == 2:
                
