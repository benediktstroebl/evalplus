
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
    month_indices = [0,3,5,7,8,10,12]
    date_indices = [4,6,9,11]
    month_range = [(1, 12), (1, 12)]
    date_range = (4,29)
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    def get_valid_month_indices(month_name):
        for i, m in enumerate(month_range):
            if month_name[0] == m:
                return i
        return -1
    def get_valid_date_indices(month_name):
        for i, m in enumerate(month_range):
            for j, d in enumerate(date_range):
                if month_name[1] == d and get_valid_month_indices(month_name[0]) == -1:
                    return i,j
        return -1
    month_name = date.split('/')[0]
    day_name = date.split('/')[1]
    try:
        month_index = get_valid_month_indices(month_name)
        date_index = get_valid_date_indices(day_name)
        if month_index == -1 or date_index == -1:
            return False
    except:
        return False
    
    return True