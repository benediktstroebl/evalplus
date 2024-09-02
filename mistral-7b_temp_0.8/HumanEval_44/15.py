

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
    while x:
        y = x % base
        x //= base
        if y < 10:
            return change_base(x, base) + str(y)
        return change_base(x, base) + str(y - 10)
    return '0'

