
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
    if number == 0:
        return 'z'
    mapping = {
        1: 'x',
        2: 'xs',
        3: 'x',
        4: 'x',
        5: 'v',
        6: 'vi',
        7: 'v',
        8: 'v',
        9: 'i',
        10: 'x',
        20: 'x',
        30: 'x',
        40: 'x',
        50: 'l',
        60: 'l',
        70: 'l',
        80: 'l',
        90: 'xl',
        100: 'x',
        200: 'xc',
        300: 'xc',
        400: 'xc',
        500: 'd',
        600: 'dc',
        700: 'd',
        800: 'd',
        900: 'xcd',
        1000: 'm'
    }
    if number in mapping:
        return mapping[number]
    for key, value in mapping.iteritems():
        if key > number:
            return value + mapping[key-number]
    return

