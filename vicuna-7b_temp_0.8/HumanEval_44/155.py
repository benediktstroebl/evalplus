

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
    digit = 0
    str_x = ''
    while x > 0:
        digit = x % base
        x = x // base
        str_x = digit + str_x
    return str_x