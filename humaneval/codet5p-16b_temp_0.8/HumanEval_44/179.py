

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

    base_digits = '0123456789ABCDEF'
    if x < 0:
        return change_base(-x, base)
    result = ''
    while x > 0:
        result = base_digits[x % base] + result
        x //= base
    return result
