

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
    # base=2 returns '10', base=3 returns '33'
    if base == 2:
        return str(x/3)[2:] * 3 + str(x%3)[2:]
    elif base == 3:
        return str(x/3)[2:] * 3
    else:
        return str(x/base)[2:] * base
