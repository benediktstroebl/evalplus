
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    if number > 1000:
        raise ValueError("Sorry, number too large")

    # This list is for the roman equivalent of the values of a single digit
    roman_list = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']

    # This list is for the roman equivalent of the values of a 5 digit number
    roman_list_5 = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']

    # This list is for the roman equivalent of the values of a 10 digit number
    roman_list_10 = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']

    # This list is for the roman equivalent of the values of a 50 digit number
    roman_list_50 = ['', 'd', 'dd', 'ddd', 'di', 'ii', 'iii', 'iv', 'v', 'vi']

    # This list is for the roman equivalent of the values of a 100 digit number
    roman_list_100 = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']

    # This list is for the roman equivalent of the values of a 500 digit number
    roman_list_500 = ['', 'd', 'dd', 'ddd', 'di', 'ii', 'iii', 'iv', 'v', 'vi']

    # This list is for the roman equivalent of the values of a 1000 digit number
    roman_list_1000 = ['','m','mm','mmm','mcm', 'cm', 'ccc','cc', 'c', 'c']

    roman_str = ''

    # This loop will determine the largest number that is less than or equal to
    # the number, and add the equivalent roman equivalent to the string
    if number >= 100:
        roman_str += roman_list_100[number // 100]
        number = number % 100

    if number >=
