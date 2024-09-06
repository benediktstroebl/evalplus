

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
    # convert to decimal
    d = x // (base**-1)
    # convert to binary
    b = bin(d)[2:]  # exclude leading '1'
    # convert back to decimal
    n = sum([int(b[i]) for i in range(0, len(b), 2)])
    return str(n)
