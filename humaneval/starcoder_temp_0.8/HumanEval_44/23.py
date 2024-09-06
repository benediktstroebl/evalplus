

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
    new_base = 0
    if x < 0:
        sign = -1
    else:
        sign = 1
    x *= sign
    while x >= base:
        x, r = divmod(x, base)
        new_base += r * (base ** (len(str(x)) - 1))
    new_base += x * (base ** (len(str(x)) - 1))
    return str(new_base * sign)
