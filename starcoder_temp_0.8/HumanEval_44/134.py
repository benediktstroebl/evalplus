

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
    base_digits = '0123456789ABCDEF'
    output_str = ''
    while x > 0:
        output_str = base_digits[x % base] + output_str
        x = x // base
    return output_str

