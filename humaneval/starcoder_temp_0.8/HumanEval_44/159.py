

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
    if base > 10:
        raise ValueError("Base can't be greater than 10.")

    if x < 0:
        sign = "-"
        x = -x
    elif x == 0:
        return '0'
    else:
        sign = ''

    s = []
    while x > 0:
        x, r = divmod(x, base)
        s.append(str(r))
    return sign + ''.join(reversed(s))
