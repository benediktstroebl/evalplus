
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

    if date == '':
        return False
    l = date.split('-')
    if len(l)!= 3:
        return False
    month = l[0]
    day = l[1]
    year = l[2]
    if int(year) < 1000 or int(year) > 3000:
        return False
    if month not in ['1','2','3','4','5','6','7','8','9','10','11','12']:
        return False
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > months[int(month)-1]:
        return False
    if int(day) < 1 or int(day) > 29 and int(month) == 2:
        return False
    if int(day) < 1 or int(day) > 30 and int(month) == 4 or int(day) < 1 or int(day) >
