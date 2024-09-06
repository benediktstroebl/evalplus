
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

    # convert date string to list
    date_split = date.split("-")

    # check if date length is 3
    if len(date_split) != 3:
        return False

    # check date format
    if len(date_split[0]) != 2 or len(date_split[1]) != 2 or len(date_split[2]) != 4:
        return False

    # check date length
    if int(date_split[1]) < 1 or int(date_split[1]) > 31:
        return False
    elif (int(date_split[0]) == 1 or int(date_split[0]) == 3 or int(date_split[0]) == 5 or int(date_split[0]) == 7 or int(date_split[0]) == 8 or int(date_split[0]) == 10 or int(date_split[0]) == 12) and (int(date_split[1]) < 1 or int(date_split[1]) > 31):
        return False
    elif (int(date_split[0]) == 4 or int(date_split[0]) == 6 or int(date_split[0]) == 9 or int(date_split[0]) == 11) and (int(date_split[1]) < 1 or int(date_split[1]) > 30):
        return False
    elif int(date_split[0]) == 2 and (int(date_split[1]) < 1 or int(date_split[1]) > 29):
        return False

    # check month
    if int(date_split[0]) < 1 or int(date_split[0]) > 12:
        return False

    # check year
    if int(date_split[2]) < 0:
        return False

    # return True if the date is valid otherwise False
    return True


