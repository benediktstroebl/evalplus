
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
    sep_date = date.split('-')
    date_in_string = str(sep_date[0])+sep_date[1]
    month_index = 0
    day_index = 0
    try:
        month_str = sep_date[0]
        day_str = sep_date[1]
        year_str = sep_date[2]
        month_index = month_str_to_index(month_str)
        day_index = int(day_str)
        # There is an assumption that the timezone is UTC
        # time = datetime.datetime.strptime(date_in_string, "%m-%d-%Y")
        # # timezone_local = pytz.timezone('Europe/Berlin')
        # timezone_utc = pytz.timezone('UTC')
        # time_utc = timezone_utc.localize(time)
        # timezone_local = pytz.timezone('Europe/Berlin')
        # time_local = timezone_local.localize(time)
        # time_utc = time_utc.astimezone(pytz.utc)
        # time_local = time_local.astimezone(pytz.utc)
        # print(time_local)
        # print(time_utc)
        time_string = '{}-{}-{}'.format(month_index, day_index, year_str)
        return datetime.strptime(time_string, "%m-%d-%Y") <= datetime.utcnow()
    except Exception:
        return False
