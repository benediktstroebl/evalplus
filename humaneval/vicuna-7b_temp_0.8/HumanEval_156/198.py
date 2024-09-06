
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
    roman_chars = 'IVXLCDM'
    roman_numeral = ''
    for i in range(10):
        if number >= 10**i:
            roman_numeral += roman_chars[i]
            number -= 10**i
    return roman_numeral.lower()
