

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
    ascii = ""
    while x > 0:
        if x % base == 0:
            ascii += str(x // base)
            x = x // base
        else:
            ascii += str(x)
        x = x // base
    return ascii[::-1]
