

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
    if base > 10 or base < 2:
        raise ValueError("Base number must be in range 2...10")
    base = str(base)
    base = '0123456789ABCDEF'
    y = ''
    while x > 0:
        r = x % int(base[0])
        x = x // int(base[0])
        y = base[r] + y
    return
