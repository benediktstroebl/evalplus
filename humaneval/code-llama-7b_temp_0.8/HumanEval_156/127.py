
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
    int_to_roman_dict = {
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix',
        10: 'x',
        20: 'xx',
        30: 'xxx',
        40: 'xl',
        50: 'l',
        60: 'lx',
        70: 'lxx',
        80: 'lxxx',
        90: 'xc',
        100: 'c',
        200: 'cc',
        300: 'ccc',
        400: 'cd',
        500: 'd',
        600: 'dc',
        700: 'dcc',
        800: 'dccc',
        900: 'cm',
        1000: 'm'
    }

    div_by_10_number = number / 10
    number = number % 10

    if div_by_10_number == 1:
        roman = 'x'
    elif div_by_10_number == 2:
        roman = 'xx'
    elif div_by_10_number == 3:
        roman = 'xxx'
    elif div_by_10_number == 4:
        roman = 'l'
    elif div_by_10_number == 5:
        roman = 'll'
    elif div_by_10_number == 6:
        roman = 'lll'
    elif div_by_10_number == 7:
        roman = 'llll'
    elif div_by_10_number == 8:
        roman = 'lllll'
    elif div_by_10_number == 9:
        roman = 'llllll'
    else:
        roman = ''

    return roman + int_to_roman_dict[number]
