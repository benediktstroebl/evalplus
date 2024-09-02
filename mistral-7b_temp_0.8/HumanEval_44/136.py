

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
        raise ValueError('base cannot be larger than 10')
    if base <= 1:
        raise ValueError('base cannot be lower than 1')
    if x <= 0:
        raise ValueError('Input x cannot be less or equal to zero')
    else:
        return x
