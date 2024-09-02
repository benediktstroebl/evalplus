

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
    x = str(x)
    if base < 10:
        return x
    elif base == 10:
        return x
    else:
        return change_base(int(x, base), 10)
