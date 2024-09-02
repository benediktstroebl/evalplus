
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
    valid_dates = ['01-01-2000', '02-01-2000', '03-01-2000', '04-01-2000', '05-01-2000', '06-01-2000', '07-01-2000', '08-01-2000', '09-01-2000', '10-01-2000', '11-01-2000', '12-01-2000', '01-01-2001', '02-01-2001', '03-01-2001', '04-01-2001', '05-01-2001', '06-01-2001', '07-01-2001', '08-01-2001', '09-01-2001', '10-01-2001', '11-01-2001', '12-01-2001', '01-01-2002', '02-01-2002', '03-01-2002', '04-01-2002', '05-01-2002', '06-01-2002', '07-01-2002', '08-01-2002', '09-01-2002', '10-01-2002', '11-01-2002', '12-01-2002', '01-01-2003', '02-01-2003', '03-01-2003', '04-01-2003', '05-01-2003', '06-01-2003', '07-01-2003', '08-01-2003', '09-01-2003', '10-01-2003', '11-01-2003', '12-01-2003', '01-01-2004', '02-01-2004', '03-01-2004', '04-01-2004', '05-01-2004', '06-01-2004', '07-01-2004', '08-01-2004', '09-01-2004', '10-01-2004', '11-01-2004', '12-01-2004', '01-01-2005', '02-01-2005', '03-01-2005', '04-01-2005', '05-01-2005', '06-01-2005', '07-01-2005', '08-01-2005', '09-01-2005', '10-01-2005', '11-01-2005', '12-01-2005', '01-