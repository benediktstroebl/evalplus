

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
    x_list = []
    if base >= 10:
        raise ValueError("base number must be less than 10")
    while x > 0:
        x_list.append(x % base)
        x = x // base
    x_list.reverse()
    return "".join(str(i) for i in x_list)
