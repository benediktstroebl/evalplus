
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
    def is_leap_year(year):
        leap_years = {
            '1899': True,
            '1900': True,
            '1901': False,
            '1902': False,
            '1904': False,
            '1907': True,
            '1908': True,
            '1909': True,
            '1910': False,
            '1912': False,
            '1913': True,
            '1914': True,
            '1915': False,
            '1916': True,
            '1917': True,
            '1918': False,
            '1919': False,
            '1920': False,
            '1921': False,
            '1922': False,
            '1923': False,
            '1924': False,
            '1925': False,
            '1926': False,
            '1927': False,
            '1928': False,
            '1929': False,
            '1930': False,
            '1931': False,
            '1932': False,
            '1933': False,
            '1934': False,
            '1935': False,
            '1936': False,
            '1937': False,
            '1938': False,
            '1939': False,
            '1940': False,
            '1941': False,
            '1942': False,
            '1943': False,
            '1944': False,
            '1945': False,
            '1946': False,
            '1947': False,
            '1948': False,
            '1949': False,
            '1950': False,
            '1951': False,
            '1952': False,
            '1953': False,
            '1954': True,
            '1955': False,
            '1956': False,
            '1957': False,
            '1958': False,
            '1959': False,
            '1960': False,
            '1961': False,
            '1962': False,
            '1963': False,
            '1964': False,
            '1965':