
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
    # Note: I'm using integers in the test cases below, but the
    # 'int_to_mini_roman' function only accepts str input, so the
    # input will always be a string representation of an integer.
    # See: https://docs.python.org/3.7/library/functions.html#int

    if number < 1 or number > 1000:
        raise ValueError('Error: Number must be between 1 and 1000.')

    romans = {
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
        80: 'lxx',
