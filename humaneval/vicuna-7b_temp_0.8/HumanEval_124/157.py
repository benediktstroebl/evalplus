
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
        month = int(date[0]) - 1
        day = int(date[1])
        year = int(date[2])
        if day < 1 or day > 31:
            if year in [2013, 2014, 2015, 2016]:
                if month < 1 or month > 12:
                    return False
            elif year in [2012, 2017, 2018, 2019]:
                if month < 2 or month > 12:
                    return False
        if not (day >= 1 and day <= 31):
            return False
        if not (year >= 2000 and year <= 2020):
            return False
        if day >= 29 and year in [2012, 2017, 2018, 2019]:
            return False
        if day == 29 and year in [2020, 2021]:
            return True
        if day == 28 and year in [2000, 2001, 2003, 2005, 2007, 2008, 2010, 2012, 2016, 2019]:
            return True
        if day == 30 and year in [2006, 2011]:
            return True
        return True
    except ValueError:
        return False

@with_setup(setup=setup, teardown=teardown)
