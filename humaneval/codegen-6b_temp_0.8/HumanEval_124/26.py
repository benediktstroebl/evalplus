
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
    list = date.split("-")
    if len(list) == 3:
        list_int = [int(i) for i in list]
        if len(list_int) == 3:
            if(len(list_int[1]) == 2 and len(list_int[2]) == 4):
                if list_int[0] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                    if list_int[1] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                        if list_int[2] < 1946 and list_int[2] > 1970:
                            return True
                elif list_int[0] in ['04','05','06','07','08','09','10','11','12']:
                    if list_int[1] in ['04','05','06','07','08','09','10','11','12']:
                        if list_int[2] < 2000 and list_int[2] > 2000:
                            return True
            elif len(list_int[1]) == 1 and len(list_int[2]) == 1:
                if list_int[0] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                    if list_int[1] in ['01','02','03','04','05','06','07','08','09','10','11','12']:
                        if list_int[2] < 1946 and list_int[2] > 1970:
                            return True
                elif list_int[0] in ['04','05','06','07','08','09','10','11','12']:
                    if list_int[1] in ['04','05','06','07','08','09','10','11','12']:
                        if list_int[2] < 2000 and list_int[2] > 2000:
                            return True
        elif len(list_int[1]) == 2 and len(list_int[2]) == 2:
            if list_int[0] in ['01','02','03','04','05','