

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
    digits = '0123456789ABCDEF'
    if x < 0:
        sign = -1
    elif x == 0:
        return digits[0]
    else:
        sign = 1
    x *= sign
    digits_of_x = []
    while x:
        digits_of_x.append(digits[x % base])
        x //= base
    if sign < 0:
        digits_of_x.append('-')
    digits_of_x.reverse()
    return ''.join(digits_of_x)
