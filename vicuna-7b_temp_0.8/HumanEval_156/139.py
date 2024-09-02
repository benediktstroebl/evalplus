
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
    roman_numeral = ""
    numerator = number
    denominator = 10

    while numerator != 0:
        numerator, denominator = (numerator // 10, numerator % 10)
        roman_numeral = (roman_numeral + str(denominator).zfill(2) + "I").zfill(2)

    return roman_numeral.lower()
