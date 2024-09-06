
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
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [2, 4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [2, 4, 6, 9, 11]

    input_date = date.split('-')
    if int(input_date[2]) < 0:
        return False
    if len(input_date[0]) == 0 or len(input_date[1]) == 0 or len(input_date[2]) == 0:
        return False
    if len(input_date[0]) != 2 or len(input_date[1]) != 2 or len(input_date[2]) != 4:
        return False
    if int(input_date[1]) not in month_31 and int(input_date[1]) not in month_30:
        return False

    if input_date[1] == 2:
        if int(input_date[2]) < 0 or int(input_date[2]) > 29:
            return False
    else:
        if int(input_date[1]) in month_31 and int(input_date[2]) < 0 or int(input_date[2]) > 30:
            return False
        if int(input_date[1]) in month_30 and int(input_date[2]) < 0 or int(input_date[2]) > 31:
            return False
    if int(input_date[0]) not in days_31 and int(input_date[0]) not in days_30:
        return False
    return True

