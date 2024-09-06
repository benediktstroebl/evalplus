

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
    if base < 10:
        return str(x * (10 ** len(str(base)) - 1))[len(str(base)) - 1:]
    elif base == 10:
        return str(x)
    else:
        return str(x) + '0' * (len(str(base)) - len(str(x)))
