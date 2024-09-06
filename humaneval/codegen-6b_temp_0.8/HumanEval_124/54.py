
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
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    date = date.lower()
    if len(date) == 0:
        return False
    else:
        data = date.split('-')
        if len(data) != 3:
            return False
        try:
            int(data[0])
            int(data[1])
            int(data[2])
        except:
            return False
        if int(data[2]) < 1900:
            return False
        if int(data[0]) == 0 or int(data[1]) == 0:
            return False
        if int(data[0]) > 12 or int(data[1]) > 12:
            return False
        if int(data[0]) in months and int(data[1]) > 31:
            return False
        if int(data[1]) in months and int(data[2]) > 2020:
            return False
        if int(data[1]) in months and int(data[2]) < 1:
            return False
        if int(data[1]) in months and int(data[0]) > 29:
            return False
        if int(data[1]) in months and int(data[0]) < 1:
            return False
        return True

