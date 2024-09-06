

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
    if base < 2:
        raise ValueError
    if base == 2:
        return change_base(x, 2)
    result = ''
    while True:
        x, d = x // base, x % base
        if d >= 10:
            result += chr(55 + d)
        else:
            result += str(d)
        if x == 0:
            break
    return result[::-1]

