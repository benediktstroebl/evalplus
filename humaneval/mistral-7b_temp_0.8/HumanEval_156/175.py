
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

    assert 1 <= number <= 1000, 'Number should be greater than or equal to 1 and less than or equal to 1000'

    roman_digits = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_string = ''
    remainder = number
    for key, value in roman_digits.items():
        while remainder >= key:
            roman_string += value
            remainder -= key

    return roman_string

