

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
    if base == 2:
        x = bin(x)[2:]
    elif base == 8:
        x = oct(x)[2:]
    else:
        x = hex(x)[2:]
    return x

