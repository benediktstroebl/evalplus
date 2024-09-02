

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
    if x < 0:
        raise ValueError('The number has to be positive')
    digits = []
    while x > 0:
        x, rem = divmod(x, base)
        digits.append(str(rem))
    return ''.join(digits)

