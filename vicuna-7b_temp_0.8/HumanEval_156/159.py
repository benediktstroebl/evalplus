
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
    roman = []
    numerator = number // 1000
    while numerator != 0:
        numerator, remainder = numerator // 100, numerator % 100
        roman.append(str(remainder))
    numerator = number // 100
    while numerator != 0:
        numerator, remainder = numerator // 10, numerator % 10
        roman.append(str(remainder))
    numerator = number
    while numerator >= 1000:
        numerator, remainder = numerator // 100, numerator % 100
        roman.append(str(remainder))
    numerator = numerator // 100
    if numerator > 0:
        roman.append(str(numerator))
    return ''.join(roman)
