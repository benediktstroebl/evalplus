

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
    if not isinstance(x, int):
        raise TypeError('Only integers are allowed.')
    if not (0 < base < 11):
        raise ValueError('base should be between 0 and 11')
    if not (0 <= x < base):
        raise ValueError('number is not valid in base')
    if base == 10:
        return str(x)
    return bin(x)[2:]
