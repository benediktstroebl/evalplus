

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
        return -1
    if x == 0 or base == 10:
        return str(x)
    if x < 10:
        return str(x)
    new = ''
    while x > 0:
        digit = x % base
        if digit < 10:
            new = str(digit) + new
        else:
            new = chr(ord('A') + digit - 10) + new
        x //= base
    return new

