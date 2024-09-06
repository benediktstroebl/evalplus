
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
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
              'Sep', 'Oct', 'Nov', 'Dec']

    # Validate date
    if not date:
        return False

    # Validate number of days
    days = date.split('-')
    if len(days) == 3:
        day = days[1]
        month = days[0]
        year = days[2]
        if int(day) <= 0:
            return False
        if int(day) >= 31 and ((month == '01' or month == '03' or
                               month == '05' or month == '07' or
                               month == '08' or month == '10' or
                               month == '12')):
            return False
        if int(day) >= 30 and ((month == '04' or month == '06' or
                               month == '09' or month == '11')):
            return False
        if int(day) >= 29 and month == '02':
            return False

    # Validate month
    if len(months) < 1 or len(months) > 12:
        return False

    # Validate date format
    if len(date) != 10:
        return False
    month, day, year = date.split('-')
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > 31:
        return False
    if int(year) < 1000:
        return False

    return True

