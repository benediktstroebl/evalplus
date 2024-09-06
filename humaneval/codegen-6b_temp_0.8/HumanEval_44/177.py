

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
    if x <= 0:
        return 0
    if x >= 10:
        return x
    if x == 1:
        return base
    if x <= 3:
        return x
    if base == 10:
        return x
    if base == 2:
        return bin(x)[2:]
    if base == 8:
        return oct(x)[2:]
    if base == 16:
        return hex(x)[2:].upper()
    return change_base(x//base, base) + str(x%base)
