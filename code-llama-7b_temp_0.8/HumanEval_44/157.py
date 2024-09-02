

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
        raise ValueError('x should be positive number')
    if base < 2:
        raise ValueError('base should be greater than 1')

    converted = ''
    while x >= 1:
        div = x // base
        mod = x % base
        converted += str(mod)
        x = div
    return converted[::-1]
