
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
    try:
        # checking that the input date is not empty
        if date == "":
            return False
        # splitting the input date with '-'
        date = date.split("-")
        month = date[0]
        day = date[1]
        year = date[2]
        # checking the length of the input date
        if len(date) != 3 or len(month) != 2 or len(day) != 2 or len(year) != 4:
            return False
        # checking the range of the month
        if int(month) < 1 or int(month) > 12:
            return False
        # checking the range of the day
        if int(day) < 1 or int(day) > 31:
            return False
        # checking the format of the date
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        # checking the range of the year
        if int(year) < 1 or int(year) > 2099:
            return False
        # checking the date
        if int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
            if int(day) < 1 or int(day) > 31:
                return False
        elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
            if int(day) < 1 or int(day) > 30:
                return False
        elif int(month) == 2:
            if int(day) < 1 or int(day) > 29:
                return False
        else:
            return False
        return True
    except:
        return False

