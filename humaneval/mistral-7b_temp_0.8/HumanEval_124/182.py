
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
    string_date = date.strip()
    date_list = string_date.split("-")

    if len(date_list) != 3 or string_date == "":
        return False

    date1 = date_list[0]
    date2 = date_list[1]
    date3 = date_list[2]

    if date1.isdigit() and date2.isdigit() and date3.isdigit():
        month_int = int(date1)
        day_int = int(date2)
        year_int = int(date3)
        month = "mm-dd-yyyy"

        if month_int in range(1, 13) and day_int in range(1, 32) and year_int in range(1900, 2022):

            if month_int in [1, 3, 5, 7, 8, 10, 12]:
                if day_int <= 31:
                    return True
                else:
                    return
