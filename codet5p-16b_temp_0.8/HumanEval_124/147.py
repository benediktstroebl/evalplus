
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

    months = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}

    if len(date) == 0:
        return False
    else:
        date = date.split('-')
        if len(date)!= 3:
            return False
        else:
            for i in range(len(date)):
                try:
                    date[i] = int(date[i])
                except:
                    return False
            if date[1] in months:
                if date[0] >= 1 and date[0] <= months[str(date[1])]:
                    if date[0] == 2 and date[1] == 1:
                        if date[2] % 4 == 0 and date[2] % 100!= 0:
                            if date[2] % 400 == 0:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
