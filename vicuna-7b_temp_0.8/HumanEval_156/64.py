
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
    radix = 10

    while number > 0:
        number, rem = divmod(number, radix)
        if rem != 0:
            digit = rem + 'A' - 10
        else:
            digit = rem + 'A'
        roman = digit + roman

    return roman.lower()