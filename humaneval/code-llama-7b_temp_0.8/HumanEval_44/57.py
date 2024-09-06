

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
    if not x:
        return '0'
    if x <= 0:
        raise ValueError("input must be positive")
    a = ''
    while x > 0:
        a = str(x % base) + a
        x //= base
    return a
