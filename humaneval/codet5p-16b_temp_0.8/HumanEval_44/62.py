

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

    result = ''
    x_base_10 = x
    while x_base_10 > 0:
        result = str(x_base_10 % base) + result
        x_base_10 //= base
    return result

