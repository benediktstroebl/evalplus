

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
    res = ''
    base_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while x!= 0:
        n = x % base
        res = str(base_list[n]) + res
        x = x // base
    return res

