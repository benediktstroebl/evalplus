

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
        result = str(x)
    elif base == 2:
        while x > 1:
            result = str(x % 2) + result
            x //= 2
    else:  # base == 8
        while x > 1:
            result = str(x % 8) + result
            x //= 8
    return result

