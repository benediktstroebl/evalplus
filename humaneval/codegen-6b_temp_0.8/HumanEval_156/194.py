
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
    if number < 1 or number > 1000:
        return 'italy?'

    for i, r in enumerate(ROMANS):
        if number - i > 0:
            roman += r
            number -= i

    return roman.lower()
