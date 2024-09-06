
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
    remainder = 0
    while number > 0:
        remainder = number % 10
        number //= 10
        if remainder >= 4:
            roman = 'I' + roman
        elif remainder >= 3:
            roman = 'V' + roman
        elif remainder >= 2:
            roman = 'X' + roman
        else:
            roman = 'X' + 'V' + roman
    if number > 0:
        roman = 'X' + roman
    return roman.lower()
