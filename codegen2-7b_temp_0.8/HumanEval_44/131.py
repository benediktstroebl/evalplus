

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
    base = 10 if base < 10 else base
    sign = ""
    if x < 0:
        sign = "-"
        x = abs(x)
    x = str(x)
    if base == 10:
        return x
    while x:
        x, remainder = divmod(x, base)
        yield remainder + 97 if remainder < 10 else remainder
