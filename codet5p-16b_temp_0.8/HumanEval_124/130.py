
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

    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    months_31 = [1,3,5,7,8,10,12]
    months_30 = [4,6,9,11]
    date = date.split('-')
    if len(date) == 3:
        if int(date[0]) > 12 or int(date[0]) < 1:
            return False
        if int(date[0]) in months_31 and int(date[1]) > 31 or int(date[0]) in months_30 and int(date[1]) > 30 or int(date[0]) == 2 and int(date[1]) > 29:
            return False
        return True
    else:
        return False







