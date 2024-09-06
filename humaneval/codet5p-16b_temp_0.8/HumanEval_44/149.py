

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

    x_str = str(x)
    x_str_len = len(x_str)
    y_str_len = len(change_base(x_str_len, base))
    y = 0
    for i in x_str:
        y = y + int(i) * base ** x_str_len
        x_str_len -= 1
    return str(y).rjust(y_str_len, '0')
