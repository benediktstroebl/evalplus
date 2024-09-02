

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
        sign = '-'
        x = abs(x)
    else:
        sign = ''
    x_str = str(x)
    if base > 10:
        return 'Invalid base.'
    if x < base:
        return sign + x_str
    digs = []
    while x:
        digs.append(x % base)
        x //= base
    if digs[-1] == 0:
        digs = digs[:-1]
    digs.reverse()
    return sign + ''.join(map(str, digs))
