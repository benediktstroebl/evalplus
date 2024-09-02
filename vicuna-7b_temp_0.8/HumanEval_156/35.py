
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
    roman = ''
    numerator = number // 1000
    denominator = number
    while denominator != 0:
        numerator, denominator = denominator // 100, denominator % 100
        roman = f'{roman}{numerator:d}{numerator > 0 ? 'I' : 'i'}{denominator:d}' if denominator > 0 else f'{roman}{numerator:d}{numerator > 0 ? 'I' : 'i'}{denominator:d}'
    return lowercase(roman)
