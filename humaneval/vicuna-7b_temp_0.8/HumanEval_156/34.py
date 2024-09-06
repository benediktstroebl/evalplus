
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
    roman_chars = 'I V X L C D'.split()
    roman_numeral = ''
    for i in range(len(str(number))):
        digit = str(number)[i]
        if digit.isdigit():
            value = digit - '0'
            roman_numeral = roman_chars[value] + roman_numeral
    return roman_numeral.lower()