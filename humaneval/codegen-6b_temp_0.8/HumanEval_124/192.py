
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
    months = [1,3,5,7,8,10,12]
    days = [31,30,31,30,31,30,31,31]
    date = date.split("-")
    if len(date) != 3:
        return False
    for i in range(len(date)):
        if len(date[i]) != 2:
            return False
        if len(date[i]) == 1:
            if (ord(date[i][0]) < 48) or (ord(date[i][0]) > 57):
                return False
        if i == 1:
            if int(date[i]) <= 0 or int(date[i]) > 31:
                return False
        if i == 2:
            if int(date[i]) <= 0 or int(date[i]) > 12:
                return False
        if i == 0:
            if int(date[j]) <= 0 or int(date[j]) > 12:
                return False
    return True
