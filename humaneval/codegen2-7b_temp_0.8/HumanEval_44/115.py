

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
    if base >= 10:
        raise ValueError
    while x > 0:
        base_10 = x % 10
        x //= 10
        rem = (x % base)
        yield base_10 if rem == 0 else rem
