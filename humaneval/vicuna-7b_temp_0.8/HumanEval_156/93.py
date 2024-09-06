
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
    numerator, denom = divmod(number, 1000)
    numerator, denom = divmod(numerator, 100)
    numerator, denom = divmod(numerator, 10)
    numerator, denom = divmod(numerator, 10)
    roman_numeral = str(numerator)
    for i in range(len(denom) - 1, -1, -1):
        roman_numeral += str(denom[i])
    return roman_numeral.lower()
