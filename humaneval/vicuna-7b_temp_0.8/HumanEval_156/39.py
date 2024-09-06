
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
    factor = 1000
    while factor >= 10:
        factor /= 10
        roman_numerals.append(str(factor))
    roman_numerals.insert(0, str(number % 1000))
    roman_numerals.reverse()
    return ''.join(roman_numerals)
