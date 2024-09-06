
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
    # regexp to match the date format
    valid_date_reg = re.compile(r'^([0-2]{1}|[0-9]{1})[-/.]' +
                                r'([0-3]{1}|[0-9]{1})' +
                                r'[-/.]([0-9]{4})$')
    
    if valid_date_reg.match(date) == None:
        return False
    
    # converts string to list with corresponding indexes
    date_list = [int(x) for x in re.split('-',date)]
    
    # 1. the date string is not empty
    if len(date_list) == 0:
        return False

    # 2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2
    if date_list[0] < 1 or date_list[0] > 31 and date_list[0] < 32 and date_list[0] > 29 and date_list[0] < 30 and date_list[0] < 99 and date_list[0] > 99:
        return False

    if date_list[1] < 1 or date_list[1] > 12:
        return False

    # 3. The months should not be less than 1 or higher than 12
    if date_list[0] == 2 and date_list[1] < 1:
        return False

    # 4. The date should be in the format: mm-dd-yyyy
    if date_list[1] < 1 or date_list[1] > 31 or date_list[2] < 0 or date_list[2] > 9999:
        return False

    return True
