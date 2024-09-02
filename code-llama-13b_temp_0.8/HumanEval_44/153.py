

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
    if x < 0 or base < 0:
        raise ValueError
    if base == 1:
        return '1' * x
    elif base == 2:
        result = ""
        while x > 0:
            x, remainder = divmod(x, 2)
            result = str(remainder) + result
        return result
    elif base == 10:
        return str(x)
    else:
        num = ""
        while x >= base:
            x, remainder = divmod(x, base)
            num = str(remainder) + num
        return str(x) + num

