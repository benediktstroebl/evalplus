
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
    valid = False
    if len(date) == 10:
        if date[2] == '-' and date[5] == '-':
            try:
                if date[6:10].isdigit():
                    year = int(date[6:10])
                else:
                    year = 0
                if date[0:2].isdigit():
                    month = int(date[0:2])
                else:
                    month = 0
                if date[3:5].isdigit():
                    day = int(date[3:5])
                else:
                    day = 0
                if 1 <= month <= 12:
                    if 1 <= day <= 31:
                        if month in (4, 6, 9, 11) and day <= 30:
                            valid = True
                        elif month in (1, 3, 5, 7, 8, 10, 12) and day <= 31:
                            valid = True
                        elif month == 2 and day <= 29:
                            if year % 400 == 0:
                                valid = True
                            elif year % 100 == 0 and year % 4 == 0:
                                valid = True
                            elif year % 4 == 0:
                                valid = True
                        else:
                            valid = False
                    else:
                        valid = False
                else:
                    valid = False
            except:
                valid = False
        else:
            valid = False
    else:
        valid = False
    return valid

