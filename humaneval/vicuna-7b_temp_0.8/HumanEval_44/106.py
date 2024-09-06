

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
    if base <= 9:
        result = str(x)
        while result[0] >= base:
            result = result[1:] + result[0] + str(int(result[-1]) + 1)
        return result[1:] + str(int(result[-1]) + 1)
    elif base == 10:
        return '1'
    else:
        raise ValueError