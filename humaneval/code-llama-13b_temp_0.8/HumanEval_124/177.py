
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

    valid_date = True
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if date != "":
        if date[2] == "-" and date[5] == "-":
            try:
                month = int(date[0:2])
                if month in range(1, 13):
                    day = int(date[3:5])
                    year = int(date[6:])
                    leap = False
                    if year % 400 == 0:
                        leap = True
                    elif year % 4 == 0:
                        leap = True
                        if year % 100 == 0:
                            leap = False
                    
                    if month == 2 and leap and day in range(1, 29):
                        valid_date = True
                    elif month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
                        valid_date = True
                    elif month in [4, 6, 9, 11] and day in range(1, 31):
                        valid_date = True
                    else:
                        valid_date = False
            except:
                valid_date = False
        else:
            valid_date = False
    else:
        valid_date = False

    return valid_date
