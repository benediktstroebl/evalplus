

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
    assert 2 <= base <= 10, "base is out of range: 2 <= base <= 10"
    if base == 10:
        return str(x)
    s = ''
    while x > 0:
        s = str(x % base) + s
        x = x // base
    return s
