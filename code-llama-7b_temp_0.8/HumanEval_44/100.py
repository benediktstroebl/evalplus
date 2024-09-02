

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not 2 <= base <= 10:
        raise ValueError('Base should be between 2 and 10')
    if not isinstance(x, int):
        raise TypeError('The input should be an integer')

    if x == 0:
        return 0
    elif x < 0:
        x = -x
    res = ''
    while x != 0:
        res = str(x % base) + res
        x = x // base
    return res

