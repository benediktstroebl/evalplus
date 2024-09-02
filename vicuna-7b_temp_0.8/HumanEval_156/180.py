
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
        digit = number % 1000
        number = number // 1000
        if digit >= 4:
            roman = digit + roman[0]
        else:
            roman = digit + roman[1]
        number //= 1000
    return roman.lower()
