
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
    # Split the date by the '/'
    date_split = date.split('/')

    # zip them together with the months
    date_zip = zip(months, date_split)

    # check the lenght of the date
    if len(date) != 10:
        return False

    # check the first date
    if int(date_zip[0][1][0:2]) > 12:
        return False

    # check the second date
    if int(date_zip[1][1][0:2]) > 31:
        return False

    # check the third date
    if int(date_zip[2][1][0:2]) > 31:
        return False

    # check the fourth date
    if int(date_zip[3][1][0:2]) > 29:
        return False

    # return false if any case fails
    return True

