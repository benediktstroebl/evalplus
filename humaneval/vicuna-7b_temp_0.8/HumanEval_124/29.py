
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
    month_list = ['01', '03', '05', '07', '08', '10', '12']
    days_list = [31, 30, 28, 31, 30, 31, 29]
    month_map = {
        '01': 1,
        '03': 3,
        '05': 5,
        '07': 7,
        '08': 8,
        '10': 10,
        '12': 12
    }

    date_list = date.split('-')
    for i in range(len(date_list)):
        if date_list[i] in months_list:
            month_index = date_list[i].index('0')
            day_index = date_list[i].index('d')
            if date_list[i][month_index + 1] == date_list[i][month_index + 2] or \
               date_list[i][month_index + 2] == date_list[i][month_index + 3] or \
               date_list[i][month_index + 3] == date_list[i][month_index + 4]:
                if days_list[int(date_list[i][month_index + 1]) - 1] <= int(date_list[i][day_index]) <= days_list[int(date_list[i][month_index + 4]) - 1]:
                    return True
    return False