
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
    month_check = ['01', '03', '05', '07', '08', '10', '12']
    month_check_three = ['04', '06', '09', '11']
    month_check_two = ['02']
    if date == "":
        return False
    for i in month_check:
        if int(i) == int(date[0:2]):
            if int(date[3:5]) > 31 or int(date[3:5]) < 1:
                return False
        for ii in month_check_three:
            if int(ii) == int(date[0:2]):
                if int(date[3:5]) > 30 or int(date[3:5]) < 1:
                    return False
            for iii in month_check_two:
                if int(iii) == int(date[0:2]):
                    if int(date[3:5]) > 29 or int(date[3:5])
