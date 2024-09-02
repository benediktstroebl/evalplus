
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
    # create a list of months
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # create an empty dictionary
    valid_date_dict = {}

    # split the date and store first element as date, second element as month, third element as year
    date_split = date.split('-')
    date = date_split[0]
    month = date_split[1]
    year = date_split[2]

    if len(date_split) > 3:
        return False

    # set the date to a valid date
    if (len(date) == 0 or len(month) == 0 or len(year) == 0):
        return False

    # set the year to valid year
    if len(year) == 4:
        valid_date_dict['year'] = year
    else:
        return False

    # set the month to valid month
    if len(month) == 1:
        valid_date_dict['month'] = int(month)
    else:
        return False

    # set the day to valid day
    if len(date) == 2:
        valid_date_dict['day'] = int(date)
    else:
        return False

    # check if the month is valid date
    if valid_date_dict['month'] < 1 or valid_date_dict['month'] > 12:
        return False

    # check if the month is valid date
    if valid_date_dict['day'] < 1 or valid_date_dict['day'] > 31:
        return False

    # check if the month is valid date
    if valid_date_dict['month'] == 4 or valid_date_dict['month'] == 6 or valid_date_dict['month'] == 9 or valid_date_dict['month'] == 11:
        if valid_date_dict['day'] < 1 or valid_date_dict['day'] > 30:
            return False

    # check if the month is valid date
    if valid_date_dict['month'] == 2:
        if valid_date_dict['day'] < 1 or valid_date_dict