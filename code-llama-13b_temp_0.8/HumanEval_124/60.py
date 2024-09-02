
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
    # write your code here

    # split the string by '-'
    # count number of '-' in date
    # if date has 3 '-' and date[1] has 2 and date[2] has 4 and date[0] has 2
    # then year can't be more than 4 digits
    # month and day can't be more than 2 digits
    # month and day can't be less than 1 digit
    # the month can't be less than 1 or more than 12
    # the day can't be less than 1 or more than 30 or 31

    # split the string by '/'
    # count number of '/' in date
    # if date has 3 '/' and date[1] has 2 and date[2] has 4 and date[0] has 2
    # then year can't be more than 4 digits
    # month and day can't be more than 2 digits
    # month and day can't be less than 1 digit
    # the month can't be less than 1 or more than 12
    # the day can't be less than 1 or more than 30 or 31

    # split the string by '.'
    # count number of '.' in date
    # if date has 3 '.' and date[1] has 2 and date[2] has 4 and date[0] has 2
    # then year can't be more than 4 digits
    # month and day can't be more than 2 digits
    # month and day can't be less than 1 digit
    # the month can't be less than 1 or more than 12
    # the day can't be less than 1 or more than 30 or 31

    date = date.split('-')
    if len(date) != 3:
        return False

    if date[1].isdigit():
        day = int(date[1])
        month = int(date[0])
        year = int(date[2])

        if month > 0 and month < 13:
            if day
