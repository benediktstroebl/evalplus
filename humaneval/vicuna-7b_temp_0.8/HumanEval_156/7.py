
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
    numerator, denominator = divmod(number, 1000)
    numerator_roman = []
    while numerator > 0:
        numerator, numerator_10 = divmod(numerator, 10)
        numerator_roman.append(numerator_10 + str(numerator - 10 * numerator_10))
        numerator = numerator - 10 * numerator_10
    numerator_roman.append(str(denominator))
    numerator_roman.reverse()
    return ''.join(numerator_roman)