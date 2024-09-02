
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
        800: 'dcc',
        900: 'cm',
        1000:'m',
    }

    remainder = number % 1000
    parts = []
    if remainder > 0:
        remainder = int(number % 1000)
        if remainder > 99:
            parts.append(roman[1000])
            remainder -= 1000
        if remainder > 89:
            parts.append(roman[900])
            remainder -= 900
        if remainder > 79:
            parts.append(roman[800])
            remainder -= 800
        if remainder > 69:
            parts.append(roman[700])
            remainder -= 700
        if remainder > 59:
            parts.append(roman[600])
            remainder -= 600
        if remainder > 49:
            parts.append(roman[500])
            remainder -= 500
        if remainder > 39:
            parts.append(roman[400])
            remainder -= 400
        if remainder > 29:
            parts.append(roman[300])
            remainder -= 300
        if remainder > 19:
            parts.append(roman[200])
            remainder -= 200
        if remainder > 9:
            parts.append(roman[100])
            remainder -= 100
        if remainder > 8:
           
