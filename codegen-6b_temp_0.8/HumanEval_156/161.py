
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
    symbol_table = zip(ROMAN_MAPPINGS, ROMAN_MAPPINGS)
    output = []
    roman_numeral = ''
    for symbol in reversed(ROMAN_MAPPINGS):
        if number >= symbol:
            roman_numeral += symbol
            number -= symbol

    return roman_numeral

