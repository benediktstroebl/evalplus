

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
    out = ''
    # this if-block converts the base number to string with the base
    # number provided in input.
    if (base < 10):
        while x > 0:
            r = x % base
            out = str(r) + out
            x = x // base

    else:
        for i in range(0, len(str(x))):
            if x // base**i:
                out = str(x // base**i) + out

    return out

