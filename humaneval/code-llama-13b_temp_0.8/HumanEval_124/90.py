
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

    #convert input string to list
    date_lst = date.split("-")
    #check that length of the list is 3
    if len(date_lst) == 3:
        #check that list is not empty
        if date_lst[0] != "":
            #check that the month is valid
            if 1 <= int(date_lst[0]) <= 12:
                #check that the day is valid based on the month
                if 1 <= int(date_lst[1]) <= 31:
                    #if month is february
                    if int(date_lst[0]) == 2:
                        #check that the day is valid for february
                        if 1 <= int(date_lst[1]) <= 29:
                            return True
                        #if day is not valid
                        else:
                            return False
                    #for all other months
                    else:
                        return True
                #if day is not valid
                else:
                    return False
            #if month is not valid
            else:
                return False
    #if list is empty
    else:
        return False

