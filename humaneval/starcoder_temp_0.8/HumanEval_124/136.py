
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
    if not date:
        return False
    days = date.split('-')
    if len(days) < 3:
        return False
    days = [int(x) for x in days]
    if days[0] > 12 or days[0] < 1:
        return False
    if days[1] > 31 or days[1] < 1:
        return False
    if days[2] > 2020 or days[2] < 1900:
        return False
    if days[0] == 2:
        return (days[1] > 0 and days[1] < 29)
    if days[0] % 2 == 0:
        return (days[1] > 0 and days[1] < 30)
    else:
        return (days[1] > 0 and days[1] < 31)

