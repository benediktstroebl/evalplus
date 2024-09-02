
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

    return {
        '1': 'x',
        '2': 'cl',
        '3': 'cd',
        '4': 'c',
        '5': 'd',
        '6': 'dc',
        '7': 'd',
        '8': 'dc',
        '9': 'c',
        '10': 'xc',
        '11': 'xc',
        '12': 'xci',
        '13': 'xc',
        '14': 'lx',
        '15': 'l',
        '16': 'xl',
        '17': 'x',
        '18': 'lx',
        '19': 'x',
        '20': 'l',
        '30': 'l',
        '40': 'xc',
        '50': 'l',
        '60': 'lx',
        '70': 'lx',
        '80': 'l',
        '90': 'xc',
        '100': 'c',
        '200': 'cc',
        '300': 'ccc',
        '400': '
