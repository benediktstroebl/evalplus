
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

    roman = {
        1: 'x', 2: 'cc', 3: 'ccc', 4: 'cd', 5: 'd', 6: 'dc', 7: 'dcc',
        8: 'dccc', 9: 'cm', 10: 'xc', 11: 'xcc', 12: 'xccc', 13: 'xc',
        14: 'xc', 15: 'xcc', 16: 'xcc', 17: 'xcc', 18: 'xcc', 19: 'xcc',
        20: 'cc', 30: 'ccc', 40: 'xcd', 50: 'l', 60: 'lx', 70: 'lxx',
        80: 'lxxx', 90: 'xl', 100: 'c', 200: 'cc', 300: 'ccc', 400: 'cd',
        500: 'd', 600: 'dc', 700: 'dcc', 800: 'dccc', 900: 'cm', 1000:'m'
    }
    roman_numeral = ""
    for i in range(1, number+1):
        for key, value in roman
