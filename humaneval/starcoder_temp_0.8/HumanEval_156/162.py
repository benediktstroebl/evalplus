
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

    if not 1 <= number <= 1000:
        raise ValueError('Number out of range.')

    roman_numeral = ''

    for (arabic, roman) in MINI_ROMAN_LIST:
        while number >= arabic:
            roman_numeral += roman
            number -= arabic

    return roman_numeral

