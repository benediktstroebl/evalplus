
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

    month_map = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    if len(date) == 0:
        return False
    if len(date.split('-')) == 3:
        if int(date.split('-')[0]) < 1 or int(date.split('-')[0]) > 12:
            return False
        month_name = month_map.get(date.split('-')[0])
        if month_name is None:
            return False
        if int(date.split('-')[1]) < 1 or int(date.split('-')[1]) > 31:
            return False
        if month_name == 'February' and int(date.split('-')[1]) > 28:
            return False
        if int(date.split('-')[2]) < 1
