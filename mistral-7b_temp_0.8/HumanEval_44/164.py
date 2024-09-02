

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
        return bin(x)[2:]
    elif base == 8:
        return oct(x)[2:]
    elif base == 10:
        return str(x)
    elif base == 16:
        return hex(x)[2:]
    else:
        return "invalid base"

