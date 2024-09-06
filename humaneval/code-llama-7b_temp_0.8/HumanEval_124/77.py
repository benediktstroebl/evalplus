
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
    import datetime
    def is_leap_year(year):
        return year%4==0 and year%100 !=0 or year%400 ==0

    def is_valid_date(d):
        day,month,year = d.split('-')
        day,month,year = int(day),int(month),int(year)
        if month not in range(1,13): return False
        if day not in range(1,32): return False
        if month in [1,3,5,7,8,10,12] and day not in range(1,32): return False
        if month in [4,6,9,11] and day not in range(1,31): return False
        if month==2 and day not in range(1,30): return False
        if day > datetime.datetime(year,month,29).day: return False
        return True

    if date=='': return False
    if not is_valid_date(date): return False
    return True










