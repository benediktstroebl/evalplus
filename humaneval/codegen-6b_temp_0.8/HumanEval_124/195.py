
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
    def is_int(x):
        try:
            int(x)
            return True
        except ValueError:
            return False
    
    def validate_date(date):
        if len(date) == 0:
            return False
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day, month, year = date.split('-')
        if not is_int(day) or is_int(day) and int(day) < 1:
            return False
        if not is_int(month) or is_int(month) and int(month) < 1 or is_int(month) and int(month) > 12:
            return False
        if not is_int(year) or is_int(year) and int(year) < 1:
            return False

        if month == '1' or month == '3' or month =='5' or month =='7' or month =='8' or month =='10' or month =='12':
            if not is_int(day) or is_int(day) and int(day) < 1 or is_int(day) and int(day) > days[int(month)-1]:
                return False
        elif month == '4' or month == '6' or month == '9' or month == '11':
            if not is_int(day) or is_int(day) and int(day) < 1 or is_int(day) and int(day) > days[int(month)-1]:
                return False
        elif month == '2':
            if not is_int(day) or is_int(day) and int(day) < 1:
                return False
        else:
            return False

        if int(year) % 4 == 0:
            leap_year = True
        else:
            leap_year = False
        days_in_year = 0
        if leap_year:
            days_in_year = 366
        else:
            days_in_year = 365
        
        if not is_int(day) or is_int(day) and int(day)