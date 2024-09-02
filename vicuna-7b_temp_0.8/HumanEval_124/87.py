
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
    if len(date) < 1 or len(date) > 10:
        return False
    if date[0] not in '0123456789':
        return False
    if date[1] not in '0123456789':
        return False
    if date[2] not in '0123456789':
        return False
    if int(date[2:5]) < 1 or int(date[2:5]) > 31:
        return False
    if int(date[5:7]) < 1 or int(date[5:7]) > 30:
        return False
    if int(date[7:9]) < 1 or int(date[7:9]) > 29:
        return False
    if int(date[9]) < 1 or int(date[9]) > 12:
        return False
    return True

example_input = ['01-01-2012', '05-02-2012', '03-11-2000', '06-04-2020', '06/04/2020']

for i in example_input:
    if valid_date(i):
        print("Valid date: ", i)
    else:
        print("Invalid date: ", i)
