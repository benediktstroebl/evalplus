

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
    if base <= 0 or base > 10:
        raise ValueError("base must be between 1 and 10.")
    if x < 0:
        sign = "-"
    else:
        sign = ""
    if x == 0:
        return "0"
    x = str(x)
    d = int(x, base)
    res = ""
    while d > 0:
        res = str(d % base) + res
        d //= base
