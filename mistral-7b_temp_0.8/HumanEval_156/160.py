
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
    roman_symbols = 'iMCDL'
    roman_numerals = {'i': 1, 'M': 1000, 'C': 100, 'D': 500, 'L': 50}

    result = ''
    for n in number:
        value = roman_numerals[n]
        result += roman_symbols[roman_numerals.index(n)] * value

    return result

