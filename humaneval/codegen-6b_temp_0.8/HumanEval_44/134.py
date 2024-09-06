

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
    x = int(x)
    if base < 10:
        return str(x)

    def _change_base(x: int, base: int):
        if x < base:
            return str(x)
        return _change_base(x // base, base) + str(x % base)

    return _change_base(x, base)
