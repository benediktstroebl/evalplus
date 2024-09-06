
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
    lower_roman_int_mapping = {
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
        40: 'x',
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
    }

    if number == 0:
        return ''

    power = 1

    while number > 0:
        if number == 4:
            return 'iv'
        if number == 9:
            return 'ix'
        if number == 40:
            return 'xl'
        if number == 90:
            return 'xc'
        if number == 400:
            return 'cd'
        if number == 900:
            return 'cm'
        if number >= 50:
            power *= 10
            num = number // power
            return lower_roman_int_mapping[num] + int_to_mini_roman(number % power)
        if number >= 10:
            power *= 5
            num = number // power
            return lower_roman_int_mapping[num] + int_to_mini_roman(number % power)
        if number >= 5:
            power *= 10
            return lower_roman_int_mapping[5] + int_to_mini_roman(number % power)
        if number >= 
