
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

    # def is_leap_year(year):
    #     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # def days_in_month(month, year):
    #     if month in [1, 3, 5, 7, 8, 10, 12]:
    #         return 31
    #     elif month in [4, 6, 9, 11]:
    #         return 30
    #     elif month == 2:
    #         return 29 if is_leap_year(year) else 28
    #     else:
    #         return 0

    # components = date.split('-')
    # if len(components) != 3:
    #     return False

    # year, month, day = components
    # year, month, day = int(year), int(month), int(day)

    # if month < 1 or month > 12:
    #     return False

    # return 1 <= day <= days_in_month(month, year)

    # using datetime
    import datetime
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
        return True
    except:
        return False
    
