

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
        return
    if x == 0:
        return str(0)
    else:
        x_str = str(x)
        if x_str[0] == '-':
            is_negative = True
            x_str = x_str[1:]
        else:
            is_negative = False
        return change_base(int(x_str[-1]), base) + change_base(int(x_str[:-1]), base)
