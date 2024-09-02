

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
    if base == 0:
        return ''
    x = int(x)
    if x < 0:
        return ''
    if x == 0:
        return '0'
    if base == 1:
        return str(x)
    if base == 2:
        return str(x)
    if base == 3:
        return str(x)
    if base == 4:
        return str(x)
    if base == 5:
        return str(x)
    if base == 6:
        return str(x)
    if base == 7:
        return str(x)
    if base == 8:
        return str(x)
    if base == 9:
        return str(x)
    if base == 10:
        return str(x)
    while x >= base:
        x //= base
        base += 1
    return str(x)
