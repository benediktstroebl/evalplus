

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
        return 0
    elif base == 10:
        return str(x)
    else:
        xstr = str(x)
        if x < 0:
            xstr = '-' + xstr[1:]
        return xstr[:-1] + str(int(xstr[-1]) * base)

