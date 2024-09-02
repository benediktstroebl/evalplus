

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
    if x < 0:
        sign = -1
    elif x == 0:
        return '0'
    else:
        sign = 1
    x *= sign
    digits = digits[::-1]
    res = []
    while x:
        res.append(digits[x % base])
        x //= base
    res.reverse()
    return ''.join(res)
