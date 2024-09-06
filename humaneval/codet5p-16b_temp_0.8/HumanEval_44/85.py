

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

    if x < 0:
        negative = True
        x = -x
    else:
        negative = False
    x = change_base_positive(x, base)
    if negative:
        return '-' + x
    return x

