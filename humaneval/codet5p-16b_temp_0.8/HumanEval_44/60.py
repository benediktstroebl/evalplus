

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

    assert 2 <= base <= 16
    if base == 16:
        return change_base(x, 2)

    r = ""
    while x > 0:
        r = str(x % base) + r
        x = x // base

    return r

