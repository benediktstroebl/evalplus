
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
    numerator_roman = ''.join(map(str, numerator))
    denominator_roman = ''.join(map(str, denominator))
    return ''.join(map(lambda x: 'M' if x >= 10 else x, numerator_roman)) + \
           ''.join(map(lambda x: 'C' if x >= 10 else x, denominator_roman))
