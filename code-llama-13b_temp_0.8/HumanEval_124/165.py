
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
    
    try:
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        
        if month in months and year < 2021:
            if month in (1, 3, 5, 7, 8, 10, 12):
                return day <= 31 and day >= 1
            elif month in (4, 6, 9, 11):
                return day <= 30 and day >= 1
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    return day <= 29 and day >= 1
                else:
                    return day <= 28 and day >= 1
    except:
        return False
    return False
        
    
