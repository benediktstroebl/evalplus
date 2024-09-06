

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
    """
    rev = ''
    if x < 0:
        x = -x
        negative = True
    else:
        negative = False
    while x >= 1:
        x, d = divmod(x, base)
        rev = str(d) + rev
    if negative:
        rev = '-' + rev
    return rev
    """
    result = ''
    sign = ''
    if x < 0:
        sign = '-'
        x = -x
    while x >= base:
        x, d = divmod(x, base)
        result = str(d) + result
    result = sign + str(x) + result
    return result

