

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
    assert base > 1
    assert base <= 10
    assert base >= 2
    assert type(x) == int
    assert type(base) == int
    assert x >= 0
    assert x < base**(base-1)
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    
