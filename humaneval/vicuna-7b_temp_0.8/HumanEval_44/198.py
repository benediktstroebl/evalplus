

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
    x_str = str(x)
    y = 0
    while x_str[0] >= '0':
        y = y * 10 + int(x_str[1:])
        x_str = x_str[:-1]
    return str(y)[:-1] + x_str
