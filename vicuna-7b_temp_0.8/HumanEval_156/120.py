
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
    roman_numerals = []
    numerator = number
    denominator = 1000
    while numerator != 0:
        numerator, denominator = divmod(numerator, denominator)
        roman_numerals.append(str(denominator))
    roman_numerals.insert(0, str(numerator))
    return ''.join(reversed(roman_numerals))
