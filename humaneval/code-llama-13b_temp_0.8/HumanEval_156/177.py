
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
    tens_converter = {
        1: 'x',
        5: 'l',
        10: 'c',
        50: 'd',
        100: 'm',
    }
    ones_converter = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }

    if number < 1 or number > 1000:
        raise ValueError("number must be in the range 1-1000")

    num_str = ''
    num_str += ones_converter[number % 10]
    number = number // 10
    num_str += tens_converter[number % 10]

    return num_str

