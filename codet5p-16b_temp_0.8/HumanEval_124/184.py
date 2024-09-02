
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

    valid_days = {1:31, 2:29, 4:30, 6:30, 9:30, 11:30, 12:31}
    for d in date.split('-'):
        if d.isdigit() and int(d) > 0 and len(d) <= 2:
            pass
        else:
            return False

    if len(date.split('-')) == 3 and (int(date.split('-')[0]) in valid_days.keys()) and (int(date.split('-')[0]) == 1 or int(date.split('-')[0]) == 3 or int(date.split('-')[0]) == 5 or int(date.split('-')[0]) == 7 or int(date.split('-')[0]) == 8 or int(date.split('-')[0]) == 10 or int(date.split('-')[0]) == 12) and (int(date.split('-')[1]) in valid_days.values()) and (int(date.split('-')[0]) in valid_days.keys()) and (int
