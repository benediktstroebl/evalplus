
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

    if len(date)==0: return False
    try:
        date_parts=date.split('-')
        month=int(date_parts[0])
        day=int(date_parts[1])
        year=int(date_parts[2])
        if month not in range(1,13): return False
        if day not in range(1,31): return False
        if day in range(1,31) and month in range(4,8): 
            if month==4 and day>29: return False
            if month==6 and day>30: return False
            if month==9 and day>30: return False
            if month==11 and day>30: return False
        if day in range(1,31) and month in range(8,11): 
            if month==8 and day>31: return False
            if month==10 and day>31: return False
            if month==12 and day>31: return False
        if month in range(1,3) and day in range(1,29): return False
        if month in range(5,7
