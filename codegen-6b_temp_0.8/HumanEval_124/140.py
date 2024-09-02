
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
    def valid_month(month):
        if 1 <= int(month) <= 12:
            return True
        else:
            return False

    def valid_day(day):
        if 1 <= int(day) <= 31:
            return True
        else:
            return False

    def valid_year(year):
        if 1 <= int(year) <= 999:
            return True
        else:
            return False

    date_arr = date.split('-')
    if len(date_arr) != 3:
        return False
    if False in [valid_month(date_arr[0]), valid_day(date_arr[1]), valid_year(date_arr[2])]:
        return False
    return True

