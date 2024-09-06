
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
        date_str = date.strip()
        months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        days = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        
        if re.search("\d{2}-\d{2}-\d{4}", date_str):
            # Extract the date
            date_split = date_str.split("-")
            
            # Check if the date format is correct
            if len(date_split) != 3:
                return False
            
            # Extract the month
            month = date_split[0].strip()
            if not month in months:
                return False
            
            # Get the day
            day = date_split[1].strip()
            if not day in days:
                return False
            
            # Get the year
            year = date_split[2].strip()
            if not year.isdigit():
                return False
            
            return True
        else:
            return False
    except:
        return False
    

test_cases =  [["",""], ["",""], ["",""], [""]]

for i in range(len(test_cases)):
    print("Test case: " + str(test_cases[i]))
    print(valid_date(test_cases[i][0]))

