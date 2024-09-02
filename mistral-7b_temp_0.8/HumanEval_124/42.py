
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
    # solve here
    d=date.split("-")
    if len(d)==3:
        if(len(d[0])==2 and len(d[1])==2 and len(d[2])==4):
            d1=int(d[0])
            d2=int(d[1])
            d3=int(d[2])
            if d3%4==0 and d1==2:
                if d2>28:
                    return False
            elif d1==2:
                if d2>29:
                    return False
            elif d1>12 or d1<1:
                return False
            elif d2>31 or d2<1:
                return False
            elif d3<1000 or d3>9999:
                return False
            else:
                return True
        else:
            return False
    else:
        return False
