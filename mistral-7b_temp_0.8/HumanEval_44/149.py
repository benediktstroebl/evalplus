

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
    if x < 0 or base < 2 or base > 10:
        return None
    else:
        str_base = str(base)
        return ''.join([str_base[i % len(str_base)] for i in range(int(x))])

