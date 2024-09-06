

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
    assert base <= 10
    assert base >= 2
    assert x >= 0
    sign = '' if x >= 0 else '-'
    return sign + bin(x)[2:] if base == 10 else sign + str(x)

