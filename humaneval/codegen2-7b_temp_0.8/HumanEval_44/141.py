

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
    if base < 10:
        raise ValueError('base has to be a number less than 10')
    
    sign = ''
    if x < 0:
        sign = '-'
    x = abs(x)
    return ''.join(['0' if c == '0' else (str(base ** (len(str(x))-1-i)) + c for i, c in enumerate(str(x))]) + sign
