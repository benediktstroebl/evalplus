

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
    if x < 0:
        raise ValueError("x must be >= 0")
    elif base < 0:
        raise ValueError("base must be >= 0")
    elif base == 0:
        raise ValueError("base must be != 0")
    elif base == 1:
        return '1' * x
    elif x == 0:
        return '0'
    return change_base(x // base, base) + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[x % base]

