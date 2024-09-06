
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

    month_to_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 10:31, 12:31}
    date_split = date.split('-')

    if len(date_split)!= 3:
        return False
    if date_split[0].isdigit() and date_split[1].isdigit() and date_split[2].isdigit():
        if int(date_split[0]) >= 1 and int(date_split[0]) <= 12:
            if int(date_split[0]) == 2 and int(date_split[1]) == 0:
                return len(date_split[1]) == 2 and int(date_split[2]) >= 1900
            if int(date_split[0]) not in month_to_days.keys():
                return False
            elif int(date_split[1]) < 1 or int(date_split[1]) > 31:
                return False
            else:
                return int(date_split[1]) <=
