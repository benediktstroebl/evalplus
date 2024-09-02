

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
    base_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x_str = str(x)
    x_len = len(x_str)
    if x_len > 10:
        raise ValueError("numbers over 10 digits are not supported")
    res = ''
    for i in range(x_len):
        res += x_str[i]
    
