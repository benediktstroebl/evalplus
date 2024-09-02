
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
    regex = re.compile('\d{1,2}(-|\/|\.)\d{1,2}(-|\/|\.)\d{4}', re.IGNORECASE)
    result = regex.search(date)
    if result == None or len(result.group()) < 5:
        return False

    error_string = "Day, month or year is invalid"
    if date.count('-') == 1:
        split_date = date.split('-')
        if len(split_date[0]) < 2 or len(split_date[1]) < 2 or len(split_date) > 3:
            return False
        day = split_date[0]
        month = split_date[1]
    else:
        split_date = date.split('/')
        if len(split_date[0]) < 2 or len(split_date[1]) < 2 or len(split_date) > 3:
            return False
        day = split_date[0]
        month = split_date[1]
        
    day_val = int(day)
    month_val = int(month)    
    if month_val < 1 or month_val > 12:
        return False
    if day_val < 1 or day_val > 31:
        return False

    if not len(date) == 10:
        return False
        
    if split_date[2].isdigit():
        if len(split_date[2]) < 4:
            return False
        else:
            if int(split_date[1]) > 12:
                return False
            else:
                if day_val > 30 and int(split_date[1]) == 1 and month_val == 2:
                    return False
                if day_val > 29 and int(split_date[1]) == 4 and month_val == 6 and int(split_date[2]) > 20:
                        return False                
                if day_val > 30 and int(split_date[1]) == 9 and month_val == 11:
                        return False                
                if day_val > 31 and int(split_date[1]) == 2 and month