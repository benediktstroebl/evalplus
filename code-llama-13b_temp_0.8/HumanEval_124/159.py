
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
    import re
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    months_with_30_days = ['01', '03', '05', '07', '08', '10', '12']
    months_with_31_days = ['01', '03', '05', '07', '08', '10', '12']
    regex_date = re.compile(r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$')
    if regex_date.match(date) == None:
        return False

    month, day, year = date.split('-')

    if day == '0' or day == '00':
        return False

    if month in months_with_30_days and int(day) <= 30:
        return True
    elif month in months_with_31_days and int(day) <= 31:
        return True
    elif month == '02' and int(day) <= 29:
        return True
    else:
        return False

