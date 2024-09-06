

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

    if base == 10:
        return str(x)
    if base == 2:
        return change_base(x, base = 10) if x >= 2 else '0'+str(x)
    return change_base(x // base, base=base) + str(x % base)
