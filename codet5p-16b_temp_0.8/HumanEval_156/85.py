
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

    numeral_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m'
    }
    if number > 1000:
        raise ValueError('Input number is too big')
    elif number < 1:
        raise ValueError('Input number is too small')
    result = ''
    for key in numeral_map:
        result += numeral_map[key] * (number // key)
        number = number % key
    return result.lower()

