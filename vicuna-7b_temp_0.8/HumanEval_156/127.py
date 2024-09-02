
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
    while number > 0:
        numerator = number // 1000
        number %= 1000
        roman = (numerator + 1000) + roman[numerator > 0]
        numerator = number // 100
        number %= 100
        roman = (numerator + 100) + roman[numerator > 0]
        numerator = number // 10
        number %= 10
        roman = (numerator + 10) + roman[numerator > 0]
    return roman.lower()
