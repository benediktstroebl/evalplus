

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
    if base >= 10:
        raise ValueError("Base should be less than 10")
    str_num = str(x)
    out_str = ""
    while str_num:
        num = str_num.pop()
        out_str += str(int(num) % base)
    return out_str[::-1]

