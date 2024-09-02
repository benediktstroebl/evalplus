
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
    
    # Your code here
    
    valid_date = False
    
    #Regexes to find valid dates (including the month and year)
    date_re = re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')
    month_re = re.compile(r'(\d{1,2})\-(0?[1-9]|1[0-2])-'+ str(datetime.datetime.now().year))
    
    #Regexes to find invalid dates
    invalid_day_re = re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')
    invalid_month_re = re.compile(r'(\d{1,2})\-(0?[1-9]|1[0-2])-'+ str(datetime.datetime.now().year))
    invalid_year_re = re.compile(r'(\d{1,2})\-(0?[1-2]|3[0-9])-'+ str(datetime.datetime.now().year))
    invalid_date_re = re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')

    #Validate dates
    
    #Date to validate
    valid_date = date_re.match(date)
    #Checking for invalid month
    invalid_month = month_re.match(date)
    #Checking for invalid day
    invalid_day = invalid_day_re.match(date)
    #Checking for invalid year
    invalid_year = invalid_year_re.match(date)
    #Checking for invalid date
    invalid_date = invalid_date_re.match(date)
    
    
    if valid_date and (invalid_month or invalid_day or invalid_year or invalid_date):
        return False
    else:
        return True
    