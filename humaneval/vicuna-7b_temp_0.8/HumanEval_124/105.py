
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
    try:
        date = date.split('/')
        if len(date) < 3 or len(date) > 4:
            return False
        date_list = []
        for i in date:
            if i.isdigit():
                date_list.append(i)
            else:
                date_list.append(int(i) - 1)
        month = date_list[1]
        day = date_list[2]
        year = date_list[3]
        if 1 <= month <= 12 and 1 <= day <= 31 and day > 0 and year in range(2000, 2060):
            return True
        elif 4 <= month <= 6 and 1 <= day <= 30 and day > 0 and year in range(2012, 2023):
            return True
        elif 4 <= month <= 12 and 1 <= day <= 29 and day > 0 and year in range(2020, 2060):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

months = [1, 3, 5, 7, 8, 10, 12]
days = [31, 30, 31, 30, 31, 30, 31]
for month in months:
    for day in days:
        if valid_date(f'0{month}-{day}-{year}') == True:
            print(f'Valid Date for Month:{month} and Day:{day} for Year: {year}')
        else:
            print(f'Invalid Date for Month:{month} and Day:{day} for Year: {year}')