

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
        return "{0:b}".format(x)
    if base == 8:
        return "{0:o}".format(x)
    if base == 16:
        return "{0:x}".format(x)
