
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
    # month and day dicts with days in the corresponding month
    month_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_dict = {1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31}

    # given date in split form, check if valid
    split_date = date.split("-")
    try:
        assert(len(split_date) == 3) # check for correct format (MM-DD-YYYY)
        month = int(split_date[0])
        assert(month > 0 and month < 13)
        day = int(split_date[1])
        if month in day_dict.keys():
            assert(day > 0 and day <= day_dict[month])
        else:
            assert(day > 0 and day <= month_dict[month])
        year = int(split_date[2])
        assert(year >= 0)
    except:
        return False

    return True
