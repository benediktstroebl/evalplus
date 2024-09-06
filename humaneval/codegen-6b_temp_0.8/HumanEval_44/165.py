

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
    if x < 0:
        sign = '-'
    else:
        sign = '+'
    x = abs(x)
    result = []
    while x > 0:
        digit = x % base
        if digit < 10:
            result.insert(0, chr(ord('0') + digit))
        else:
            result.insert(0, chr(ord('A') + digit - 10))
        x //= base
    result.insert(0, sign)
    return ''.join(result)

