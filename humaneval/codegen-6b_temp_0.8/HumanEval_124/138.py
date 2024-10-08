
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
    used_comparisons = 0
    
    months = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    days = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}

    date = date.split('-')
    if len(date) != 3:
        return False

    for i in range(len(date)):
        if len(date[i]) != 2:
            return False

        used_comparisons += 1
        try:
            int(date[i])
        except:
            return False
    
    if int(date[1]) < 1 or int(date[1]) > 12:
        return False

    if int(date[2]) < 1 or int(date[2]) > 35:
        return False

    if int(date[1]) == 2:
        if int(date[2]) < 1 or int(date[2]) > 29:
            return False
    else:
        if int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11:
            if int(date[2]) < 1 or int(date[2]) > months[date[1]]:
                return False
        else:
            if int(date[2]) < 1 or int(date[2]) > months[date[1]]:
                return False
    
    if int(date[0]) < 1 or int(date[0]) > 12:
        return False

    return True
