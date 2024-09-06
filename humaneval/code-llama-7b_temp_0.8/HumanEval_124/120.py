
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
    date_list = date.split("-")
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    # check for the month
    if month == '0' or month == '1' or month == '2' or month == '3' or month == '4' or month == '5' or month == '6' or month == '7' or month == '8' or month == '9':
        if int(month) >= 1 and int(month) <= 9:
            if int(day) >= 1 and int(day) <= 31:
                if int(year) >= 0 and int(year) <= 9:
                    return False
            else:
                return False
        elif int(month) >= 10 and int(month) <= 12:
            if int(day) >= 1 and int(day) <= 31:
                if int(year) >= 0 and int(year) <= 9:
                    return False
                elif int(year) >= 10 and int(year) <= 99:
                    return False
                elif int(year) >= 100 and int(year) <= 999:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
    
