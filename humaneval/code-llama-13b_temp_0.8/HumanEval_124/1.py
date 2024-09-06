
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
    
    if len(date) == 0:
        return False
    
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    year_format = '[0-9]{4}'
    month_format = '[0-9]{2}'
    day_format = '[0-9]{2}'
    month_day_format = month_format + "-" + day_format
    date_format = month_day_format + "-" + year_format

    if date.count("-") != 2:
        return False
    
    if date[2] == '-' and date[5] != '-':
        return False
    if date[2] != '-' and date[2] != '.' and date[5] == '-':
        return False
    if date[2] == '.' and date[5] != '.':
        return False
    if date[2] != '.' and date[2] != '-' and date[5] == '.':
        return False
    
    if date[2] == '.' or date[2] == '-':
        first_part = date[:2]
        second_part = date[3:5]
        third_part = date[6:]
    else:
        first_part = date[:2]
        second_part = date[2:5]
        third_part = date[5:]
    
    if first_part not in months:
        return False
    if second_part not in days:
        return False
    if third_part not in year_format:
        return False
    
    if date[2] == '.' or date[2] == '-
