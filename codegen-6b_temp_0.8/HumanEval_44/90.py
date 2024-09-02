

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
        return "0"
    if x < 0:
        sign = "-"
        x = abs(x)
    else:
        sign = ""
    x_str = ""
    while x != 0:
        x, mod = divmod(x, base)
        x_str = str(mod) + x_str
    return sign + x_str

