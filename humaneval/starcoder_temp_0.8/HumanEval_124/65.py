
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
        # getting the month and year
        month, year = date.split('-')
        # if the year is not empty
        if year:
            # if the month is not empty
            if month:
                # if the month is between 1 and 12
                if 1 <= int(month) <= 12:
                    # checking the length of the month
                    if len(month) == 2:
                        # if the day is not empty
                        if year[0] == '0':
                            # if the day is between 1 and 31
                            if 1 <= int(year[1]) <= 31:
                                # checking the length of the day
                                if len(year[1]) == 2:
                                    return True
                            # if the day is not between 1 and 31
                            else:
                                return False
                        # if the day is not empty
                        else:
                            # if the day is between 1 and 30
                            if 1 <= int(year[0]) <= 30:
                                # checking the length of the day
                                if len(year[0]) == 1:
                                    return True
                            # if the day is not between 1 and 30
                            else:
                                return False
                    # if the length of the month is not 2
                    else:
                        return False
                # if the month is not between 1 and 12
                else:
                    return False
            # if the month is empty
            else:
                return False
        # if the year is empty
        else:
            return False
    # if the date contains nothing
    except ValueError:
        return False
    # if the date contains something else
    except IndexError:
        return False

