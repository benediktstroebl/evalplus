
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('Number must be between 1 and 1000')
    lookup = {'1': 'i', '2': 'ii', '3': 'iii', '4': 'iv', '5': 'v', '6': 'vi', '7': 'vii', '8': 'viii', '9': 'ix', '10': 'x', '11': 'xi', '12': 'xii', '13': 'xiii', '14': 'xiv', '15': 'xv', '16': 'xvi', '17': 'xvii', '18': 'xviii', '19': 'xix', '20': 'x', '30': 'l', '40': 'lx', '50': 'lxx', '60': 'lxlx', '70': 'lxxv', '80': 'lxxx', '90': 'lxxvi', '100': 'c', '200': 'cc', '300': 'ccc', '400': 'cd', '500': 'd', '600': 'dc', '700': 'dcc', '800': 'dccc', '900': 'cm', '1000': 'm'}
    result = ''
    n_reversed = number-1
    while n_reversed > 0:
        digit = n_reversed % 10
        # If the number is between 10-19, we'll need to add an 'x'
        if 10 <= n_reversed < 19:
            result = lookup[str(digit) + 'x'] + result
        else:
            result = lookup[str(digit)] + result
        n_reversed = n_reversed // 10
    return result

