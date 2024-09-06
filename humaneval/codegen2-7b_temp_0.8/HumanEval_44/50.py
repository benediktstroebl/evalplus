

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
        raise ValueError('base must be less than 10')
    base = str(base)
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    string = ''
    while x > 0:
        x, digit = divmod(x, base)
        string = digits[digit] + string
    return
