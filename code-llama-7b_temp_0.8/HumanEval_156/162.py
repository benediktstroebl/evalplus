
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

    _1000 = ('m', 'd', 'cd', 'c', 'l', 'xl', 'x', 'lx', 'ix')
    _100 = ('c', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'lx', 'ix')
    _10 = ('x', 'l', 'xc', 'x', 'ix')
    _1 = ('i', 'x', 'v', 'i', 'iv')

    roman = ''
    while number > 0:
        number, r = divmod(number, 10)
        if r == 9:
            roman += _1000[0]
            continue
        elif r == 4:
            roman += _100[3]
            continue
        if r >= 5:
            roman += _100[r // 5]
            r %= 5
        if r >= 1:
            roman += _10[r // 1]
    return roman.lower()

