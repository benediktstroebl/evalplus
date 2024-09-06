

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
    remainder = x % base
    x = int(x / base)
    if remainder == 0:
        return str(x)
    else:
        return str(x) + str(remainder)
