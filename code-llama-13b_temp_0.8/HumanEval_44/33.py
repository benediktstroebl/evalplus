

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
    if x <= 0 or base > 10:
        raise ValueError

    sign = '-' if x < 0 else ''
    x = abs(x)
    result = ''

    while x:
        result = str(x % base) + result
        x //= base

    return sign + result

