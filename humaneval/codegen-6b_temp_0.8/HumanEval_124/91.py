
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
    import re
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    date_re="[\d]{2}-\d{2}-\d{4}"
    #d=re.search(r'\d{2}.\d{2}.\d{4}',date)
    #print("len ",int(d[0])<1)
    if len(date) == 0:
        return False
    elif int(date[0:2])<1 or int(date[0:2])>12:
        return False
    elif int(date[3:5])<1 or int(date[3:5])>31:
        return False
    elif int(date[6:])<1 or int(date[6:])>29:
        return False
    elif int(date[3:5])==2:
        if int(date[0:2])<1 or int(date[0:2])>29:
            return False
        else:
            return True
    elif int(date[3:5]) not in [1,3,5,7,8,10,12]:
        return False 
    else:
        return True
    

assert(valid_date('01-01-2010') == False)
assert(valid_date('01-0-2010') == False)
assert(valid_date('03-13-2000') == False)
assert(valid_date('01-01-0101') == False)
assert(valid_date('01-01-0101-01-01-01') == False)
assert(valid_date('03-31-2000') == False)
assert(valid_date('09-29-1999') == False)
assert(valid_date('03-31-9999') == False)
assert(valid_date('03-31-2000-01-01-01') == False)
assert(valid_date('01-01-0101-01-01-01') == True)
assert(valid_date('03-31-2000-01-01-01') == True)
assert(valid_date('12