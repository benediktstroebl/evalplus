

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
    a = 0
    res = ""
    while x:
        a = x % base
        if a < 10:
            res = str(a) + res
        else:
            res = chr(a + 64) + res
        x = x // base
    return res

