
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

    if len(date) == 0:
        return False
    elif len(date) == 10:
        if date[2] == '-' and date[5] == '-':
            if date[0:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit():
                d = date.split('-')
                if 1 <= int(d[0]) <= 12:
                    if int(d[0]) in (1,3,5,7,8,10,12) and 1 <= int(d[1]) <= 31:
                        if int(d[0]) == 4 or int(d[0]) == 6 or int(d[0]) == 9 or int(d[0]) == 11:
                            if 1 <= int(d[1]) <= 30:
                                return True
                            else:
                                return False
                        elif int(d[0]) == 2:
                            if 1 <= int(d[1]) <= 29:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
                        
