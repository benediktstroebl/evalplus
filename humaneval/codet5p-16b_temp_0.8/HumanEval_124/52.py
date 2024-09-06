
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

    date = date.split("-")
    months = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    month_no = int(date[0])
    if len(date[0])!= 2 or len(date[1])!= 2 or len(date[2])!= 4:
        return False

    day_no = int(date[1])
    year_no = int(date[2])

    if month_no > 12 or month_no < 1:
        return False
    elif day_no > months[month_no] or day_no < 1:
        return False
    elif month_no == 2 and day_no > 28:
        return False
    elif month_no!= 2 and day_no > months[month_no]:
        return False
    elif month_no == 2 and day_no > 29:
        return False
    elif month_no == 4 or month_no == 6 or
