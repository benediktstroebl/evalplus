
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
    months = ['01', '03', '05', '07', '08', '10', '12']
    days = ['31', '30', '29', '28', '29', '31', '30', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']
    if (len(date) >= 10 and len(date) <= 10 and date[0] == '0' and date[3] == '0' and date[6] == '0'):
        i = 0
        for x in date:
            if x == '-' and date[i+1] != '-':
                i += 1
            elif x != '-' and date[i+1] == '-':
                return False
            else:
                i += 1

        if date[4] in months and (date[5] == '-' and date[7] == '-' and date[9] == '0' and date[11] == '0'):
            i = 0
            days[0] = 0
            for x in date:
                if x == '-' and date[i+1] != '-':
                    i += 1
                elif x != '-' and date[i+1] == '-':
                    return False
                else:
                    i += 1
            return True
        elif date[4] in months and (date[5] == '-' and date[7] == '-' and date[10] == '0' and date[12] == '0'):
            i = 0
            days[1] = 0
            for x in date:
                if x == '-' and date[i+1] != '-':
                    i += 1
                elif x != '-' and date[i+1] == '-' and date[i+2] == '0':
                    return False
                else:
                    i += 1
            return True
        elif date[4] in months and (date[5] == '-' and date[7] == '-' and date[11] == '0' and date[13] == '0'):
            i = 0
            days[2] = 0
            for