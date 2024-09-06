

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
        raise ValueError("base must >= 2")
    if x < 0:
        sign = -1
        x *= sign
    else:
        sign = 1
    res = ''
    while x:
        res = str(x % base) + res
        x //= base
    return res if sign == 1 else '-' + res
