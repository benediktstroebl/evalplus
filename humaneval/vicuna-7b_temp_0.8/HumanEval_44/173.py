

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
    result = ""
    while x > 0:
        x, n = divmod(x, base)
        result = str(n) + result
    return result.zfill(3)