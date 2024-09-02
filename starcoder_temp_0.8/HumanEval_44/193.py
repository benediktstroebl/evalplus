

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
    if base < 2 or base > 10:
        return 'INVALID INPUT'
    if x < 0:
        sign = -1
    elif x == 0:
        return 0
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(x % base)
        x //= base
    digits.reverse()
    if sign < 0:
        digits.append('-')
    return ''.join(str(d) for d in digits)
