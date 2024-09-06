

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
    # replace by real code
    x = abs(x)
    base = min(base, 10)
    if x < base and base >= 2:
        return str(x)
    result = ''
    while x >= base:
        x, mod = divmod(x, base)
        result = str(mod) + result
    result = str(x) + result
    return result

