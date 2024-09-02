
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
    r = ''
    for i in range(number):
        if i == 0 or i == 5 or i == 10:
            r += 'iv'
        elif i == 1 or i == 4 or i == 9:
            r += 'ix'
        else:
            r += 'x'
            r += 'i' * (i - 1)
    return r.lower()

