
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
        numerator = number / 1000
        number %= 1000
        roman = (numerator * 100) + roman
        if numerator == 1:
            roman = (roman * 10) + (roman.isdigit() and 1 or 0)
        else:
            roman = (roman * 9) + (roman.isdigit() and 1 or 0)
    return roman.lower()
