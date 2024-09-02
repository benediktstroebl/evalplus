
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
    if date == "":
        return False

    days = date.split('-')[1]
    months = date.split('-')[0]
    years = date.split('-')[2]

    if not months.isdigit():
        return False

    if int(months) > 12 or int(months) < 1:
        return False

    if int(years) < 2020:
        return False

    if int(days) > 31 or int(days) < 1:
        return False

    if months in ["01", "03", "05", "07", "08", "10", "12"]:
        if int(days) > 31:
            return False

    if months in ["04", "06", "09", "11"]:
        if int(days) > 30:
            return False

    if months in ["02"]:
        if int(days) > 29:
            return False

    return True
