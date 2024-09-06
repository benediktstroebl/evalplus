

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

    if base > 10 or base < 2:
        raise ValueError("Base should be less than 10 and bigger than 1")
    if base == 1:
        return str(x)
    if base == 2:
        return change_base(x, base=2)
    if x < base:
        return change_base(x, base=base)
    else:
        return str(x % base) + change_base(x // base, base=base)

