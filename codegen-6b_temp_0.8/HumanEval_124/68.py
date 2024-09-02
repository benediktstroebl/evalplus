
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
    # replace this for solution
    import calendar
    import re
    def check_date(date):
        if len(date) > 0:
            if len(date) < 10:
                print "date is too short"
                return False
            elif len(date) > 10:
                print "date is too long"
                return False
            else:
                if not re.match('\d{1,2}-\d{1,2}-\d{4}',date):
                    print "wrong date format"
                    return False
                else:
                    split_date = date.split('-')
                    if split_date[0] not in ['01','02','03','04','05','06','07','08','09','10','11', '12']:
                        print "wrong month"
                        return False
                    elif split_date[1] not in ['01','02','03','04','05','06','07','08','09','10','11', '12']:
                        print "wrong month"
                        return False
                    elif split_date[2] < '1900':
                        print "wrong year"
                        return False
                    elif split_date[0] == '00':
                        print "wrong month"
                        return False
                    elif split_date[1] == '00':
                        print "wrong day"
                        return False
                    else:
                        # date format is ok, now check the number of days 28-29, 30-31, 1-2, except the february month
                        # leap year
                        month,day,year = int(split_date[0]), int(split_date[1]), int(split_date[2])
                        if month == 2:
                            if calendar.isleap(year):
                                if day > 29:
                                    return False
                                elif day < 29:
                                    return True
                                else:
                                    return True
                            elif not calendar.isleap(year):
                                if day > 28:
                                    return False
                                elif day < 28:
                                    return True
                                else:
                                    return True
                        # not leap year
                        if month == 2:
                            if day >