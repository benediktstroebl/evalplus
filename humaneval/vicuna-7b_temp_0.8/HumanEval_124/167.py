
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
    if len(date) == 0:
        return False
    elif not date.endswith('-' + str(len(date) % 10) + '-01'):
        return False
    elif int(date[:4]) > 12 or int(date[:2]) < 1 or int(date[:2]) > 12:
        return False
    elif int(date[:2]) == 2:
        if int(date[3:5]) > 30 or int(date[3:5]) < 29:
            return False
    elif int(date[:2]) == 4:
        if int(date[3:5]) > 30:
            return False
    return True

sample_input = ["03-11-2000", "15-01-2012", "04-0-2040", "06-04-2020", "06/04/2020"]

for item in sample_input:
    print(valid_date(item))