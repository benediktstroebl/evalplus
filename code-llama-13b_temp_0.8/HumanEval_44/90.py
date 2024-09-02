

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
    if base == 10:
        return str(x)
    sign = ''
    if x < 0:
        x = -x
        sign = '-'
    i = 0
    result = ''
    while x > 0:
        remain = x % base
        x //= base
        result += str(remain)
        i += 1
    return sign + result[::-1]

