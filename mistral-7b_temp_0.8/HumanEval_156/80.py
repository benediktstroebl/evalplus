
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
    mapping = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xl',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }

    result = ''
    while number > 0:
        max_val, max_str = next((key, val) for key, val in mapping.items() if key <= number)
        result += max_str
        number -= max_val

    return result
