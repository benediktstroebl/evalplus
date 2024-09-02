

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
    if x == 0:
        return '0'
    x_abs = abs(x)
    result = ''
    while x_abs != 0:
        result = str(x_abs % base) + result
        x_abs //= base
    if x < 0:
        result = '-' + result
    return result

