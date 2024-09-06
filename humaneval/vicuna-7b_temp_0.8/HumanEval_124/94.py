
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
    import datetime
    today = datetime.datetime.today().strftime("%m-%d-%Y")
    date_str = date.strftime("%m-%d-%Y")
    if date_str == today:
        return True
    elif date_str in ["01","03","05","07","08","10","12"]:
        if len(date_str) == 3:
            if date_str[:2] not in ["01","03","05","07","08","10","12"]:
                return True
        elif len(date_str) == 4:
            if date_str[:3] not in ["01","03","05","07","08","10","12"]:
                return True
    elif date_str[:2] == "04":
        if date_str[2:4] not in ["01","03","05","07","08","10","12"]:
            return True
    elif date_str[:3] == "04":
        if date_str[3:4] not in ["01","03","05","07","08","10","12"]:
            return True
    elif date_str[:4] == "04":
        return False
    else:
        return False
