

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
    if x < 0:
        return '-' + change_base(-x, base)
    base_10 = 0
    while x > 0:
        base_10 *= base
        base_10 += x % base
        x //= base
    if base_10 == 0:
        return '0'
    return str(base_10)
