
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
    # this is the actual roman numeral
    actual = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    # this is the roman numeral that
    # is substracted when the actual
    # value is greater than 5 times the
    # base.
    minus = {
        1: 'iv',
        5: 'ix',
        10: 'xl',
        50: 'xc',
        100: 'cd',
        500: 'cm',
        1000: 'mm'
    }

    result = ''
    for base, symbol in actual.items():
        count, number = divmod(number, base)
        while count > 0:
            if base > 1 and count > 3:
                result += minus[base]
                count -= 4
            else:
                result += symbol * count
                count = 0
        number = base * number
    return result

