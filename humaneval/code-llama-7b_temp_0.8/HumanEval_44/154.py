

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

    assert 2 <= base <= 10

    out = ''
    while x > 0:
        r = x % base
        if r >= 10:
            out = chr(ord('a')+r-10) + out
        else:
            out = str(r) + out
        x = x//base
    return out

