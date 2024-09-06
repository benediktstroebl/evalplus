
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
    denominator = number // 100
    remainder = number % 100
    while numerator != 0:
        roman.append(numerator.zfill(2))
        numerator = denominator // 10
        denominator = denominator % 10
    if remainder != 0:
        roman.append(remainder.zfill(2))
    return ' '.join(roman[::-1])