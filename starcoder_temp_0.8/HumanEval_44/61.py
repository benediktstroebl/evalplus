

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
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if base < 2 or base > len(digits):
        raise ValueError('base must be between 2 and 36 inclusive')

    if x < 0:
        sign = '-'
        x = -x
    elif x == 0:
        return '0'
    else:
        sign = ''

    s = ""
    while x > 0:
        s = digits[x % base] + s
        x = x // base

    return sign + s
