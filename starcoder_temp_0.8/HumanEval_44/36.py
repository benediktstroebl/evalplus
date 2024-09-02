

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
    if not 1 < base < 10:
        raise ValueError("Base must be between 1 and 10")

    s = ""
    while x >= base:
        r = x % base
        s = str(r) + s
        x //= base
    s = str(x) + s
    return s
