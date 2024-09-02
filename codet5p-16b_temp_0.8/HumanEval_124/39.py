
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

    if not date:
        return False
    else:
        days = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
        months = {'01':12,'02':12,'03':12,'04':12,'05':12,'06':12,'07':12,'08':12,'09':12,'10':12,'11':12,'12':12}
        month, day, year = date.split('-')
        if len(day)!= 2 or len(month)!= 2 or len(year)!= 4:
            return False
        else:
            if int(month) in months.values():
                if int(day) in range(1,days[month]+1):
                    if int(year) in range(1,9999):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False


