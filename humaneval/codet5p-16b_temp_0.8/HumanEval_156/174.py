
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

    int_to_roman_dict = {
        1: 'x',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m'
    }
    roman_numeral = []
    for key in int_to_roman_dict:
        if number // key:
            number -= (key * (number // key))
            roman_numeral += [int_to_roman_dict[key]] * (number // key)

    return ''.join(roman_numeral).lower()
