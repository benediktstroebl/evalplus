

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
    if not isinstance(base, int):
        raise TypeError("base should be int")
    if base >= 10:
        raise ValueError("base should be less than 10")
    if x < 0:
        raise ValueError("number x should be non-negative")

    res = ''
    while x > 0:
        res += str(x % base)
        x //= base

    return res

