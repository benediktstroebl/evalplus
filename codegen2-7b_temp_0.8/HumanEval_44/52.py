

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
    if base > 10:
        raise ValueError("base must be less than 10")
    if base == 10:
        return str(x)
    n = str(x)
    ret = ""
    while n:
        d, n = divmod(int(n), base)
        ret = str(base - 1 - d) + ret
    return ret
