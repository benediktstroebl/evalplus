

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
    if base < 2:
        raise ValueError('Base must be greater than 1.')
    if x < 0:
        sign = '-'
    else:
        sign = ''
    digit = 0
    if x == 0:
        res = sign + '0'

    while x//base != 0:
        digit = x//base
        res = str(digit) + res
        x = x % base
    if x == 0:
        res = sign + res
    else:
        res = str(x) + res
    return res
