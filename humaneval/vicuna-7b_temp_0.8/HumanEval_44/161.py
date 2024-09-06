

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
    if base == 0:
        return ''
    if base == 1:
        return str(x)
    if base == 2:
        return str(x) + '0'
    if base == 3:
        return str(x) + '0' + str(x)
    if base == 4:
        return str(x) + '00' + str(x) + '0'
    if base == 5:
        return str(x) + '000' + str(x) + '00' + str(x)
    if base == 6:
        return str(x) + '0000' + str(x) + '000' + str(x) + '00'
    if base == 7:
        return str(x) + '00000' + str(x) + '0000' + str(x) + '0000' + str(x)
    if base == 8:
        return str(x) + '000000' + str(x) + '000000' + str(x) + '000000' + str(x)
    if base == 9:
        return str(x) + '0000000' + str(x) + '0000000' + str(x) + '0000000' + str(x) + '0000000'
    if base == 10:
        return str(x)
    return '0' * (base - 1) + str(x)
