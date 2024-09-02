

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
    x, base = int(x), int(base)
    str_rep = ""
    while x > 0:
        str_rep = str(x % base) + str_rep
        x = x // base
    return str_rep

