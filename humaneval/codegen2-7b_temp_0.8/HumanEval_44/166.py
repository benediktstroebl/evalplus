

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
    if base < 2 or base > 10:
        raise ValueError('Invalid base')
    if base == 10:
        return str(x)
    elif base == 2:
        return bin(x)[2:]
    else:
        return format(x, '0'+str(base)+'
