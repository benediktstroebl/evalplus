
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
    # convert the given date into a list
    date_as_list = date.split('-')
    # print(date_as_list)
    # create the values for the month, day and year
    month = int(date_as_list[0])
    day = int(date_as_list[1])
    year = int(date_as_list[2])

    # create the list of valid months
    months = [1,2,3,4,5,6,7,8,9,10,11,12]

    # create the list of valid days for a given month
    valid_days = [31,31,30,31,30,31,31,30,31,30,31,30]

    # create the list of valid days for a given month
    valid_leap_days = [29,31,31,30,31,30,31,31,30,31,30,31]

    # validate month
    
