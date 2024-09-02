
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
    if 1 > number or number > 1000:
        raise ValueError('Please enter a number between 1 and 1000')
    romans = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
    accumulator = ''
    while number > 0:
        for roman in range(3, 0, -1):
            if number >= roman:
                accumulator += romans[number // roman - 1]
                number -= roman
    return accumulator.lower()

