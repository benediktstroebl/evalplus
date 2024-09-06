

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
        sign = -1
    else:
        sign = 1

    x *= sign
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    if sign < 0:
        digits.append('-')
    digits.reverse()

    return ''.join(digits)

