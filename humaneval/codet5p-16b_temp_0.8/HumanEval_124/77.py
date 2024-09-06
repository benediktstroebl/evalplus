
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

    date = date.split('-')
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 10:31, 12:31}
    if len(date[0])!= 2 or len(date[1])!= 2 or len(date[2])!= 4:
        return False
    if int(date[0]) > 12 or int(date[0]) < 1 or int(date[1]) > 31 or int(date[1]) < 1:
        return False
    if date[0] in months.keys() and date[1]!= '01':
        if date[0] == '01' or date[0] == '03' or date[0] == '05' or date[0] == '07' or date[0] == '08' or date[0] == '10' or date[0] == '12':
            if int(date[1]) > months[date[0]]:
                return False
        elif date[0] == '04' or date[0] ==
