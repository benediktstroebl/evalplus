
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
    # day_in_month = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    # month = {'01':'jan', '02':'feb', '03':'mar', '04':'apr', '05':'may', '06':'jun', '07':'jul', '08':'aug', '09':'sep', '10':'oct', '11':'nov', '12':'dec'}
    # # check if date is empty or not
    # if not date:
    #     return False
    # # convert string to list
    # split_date = date.split('-')
    # # check if length of list is equal to 3
    # if len(split_date)!= 3:
    #     return False
    # # check if the day is in range 1-31
    # if int(split_date[0]) <= 31 and int(split_date[0]) >= 1:
    #     if split_date[1] in month:
    #         month_num = int(month[split_date[1]])
    #     else:
    #         return False
    # else:
    #     return False
    # if month_num in day_in_month:
    #     if int(split_date[0]) <= day_in_month[month_num]:
    #         if int(split_date[2]) <= 29 and int(split_date[2]) >= 1800:
    #             return True
    # else:
    #     return False

    day_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    month = {'01':'jan', '02':'feb', '03':'mar', '04':'apr', '
