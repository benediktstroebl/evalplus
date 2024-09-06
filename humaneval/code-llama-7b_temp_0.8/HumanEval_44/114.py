

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
    # zero is a special case
    if x == 0:
        return 0

    # get digits one by one
    res = ""
    while x:
        res += str(x % base)
        x = x // base

    return res

