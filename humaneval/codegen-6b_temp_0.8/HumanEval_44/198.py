

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
        return 0
    if base == 10:
        return str(x)

    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base

    digits = digits[::-1]
    return ''.join(str(d) for d in digits)

