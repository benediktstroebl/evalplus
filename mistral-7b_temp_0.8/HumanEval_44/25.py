

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
    if base < 10:
        if x >= 0:
            if x >= base:
                return change_base(x // base, base) + change_base(x % base, base)
            else:
                return str(x)
        else:
            if x % base == 0:
                return change_base(x // base, base)
            else:
                return '-' + change_base(x % base, base)
    else:
        return str(x)
