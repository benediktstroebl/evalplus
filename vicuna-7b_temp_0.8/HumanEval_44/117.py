

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
        return '0'
    elif base == 1:
        return '1'
    elif base == 2:
        return '2'
    elif base == 3:
        return '3'
    elif base == 4:
        return '4'
    elif base == 5:
        return '5'
    elif base == 6:
        return '6'
    elif base == 7:
        return '7'
    elif base == 8:
        return '8'
    elif base == 9:
        return '9'
    else:
        return str(x)
