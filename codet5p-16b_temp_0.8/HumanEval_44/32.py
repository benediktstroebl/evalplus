

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

    result = ''
    if base == 10:
        return str(x)
    if base == 2:
        return change_base(x, 10)
    elif base == 3:
        return change_base(x, 10)
    elif base == 4:
        return change_base(x, 10)
    elif base == 5:
        return change_base(x, 10)
    elif base == 6:
        return change_base(x, 10)
    elif base == 7:
        return change_base(x, 10)
    elif base == 8:
        return change_base(x, 10)
    elif base == 9:
        return change_base(x, 10)
    else:
        return change_base(x, base)

