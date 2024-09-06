
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
    invalid = ["/", "-"]
    date = str(date)
    year = date[6:]
    month = date[2:4]
    day = date[0:2]
    if any(invalid in date):
        return False
    if len(date) > 10 or len(date) < 10:
        return False
    if day.isdigit() and month.isdigit() and year.isdigit():
        if month.isnumeric():
            if int(month) > 12 or int(month) < 1:
                return False
        else:
            if month == "Jan" or month == "Feb" or month == "March" or month == "April" or month == "May" or month == "June" or month == "July" or month == "August" or month == "September" or month == "October" or month == "November" or month == "December":
                if day.isdigit() and int(day) > 31 or int(day) < 1:
