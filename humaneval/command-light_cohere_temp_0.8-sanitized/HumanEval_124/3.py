import datetime
def valid_date(date_str):
    """
    :type date_str: str
    :rtype: bool
    """

    date = datetime.strptime(date_str, "%m-%d-%Y")

    # convert to datetime.strftime("%Y-%m-%d")
    # check for valid year
    # check for valid month
    # check for valid day of the month
    return date.strftime("%Y-%m-%d") >= datetime.datetime(1900,1) <= datetime.datetime(2099_00)