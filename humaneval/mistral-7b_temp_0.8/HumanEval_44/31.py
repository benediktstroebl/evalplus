

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
    if base < 2 or base > 9:
        raise ValueError('base must be 2 - 9')
    if x < 0:
        raise ValueError('Negative numbers are not supported')
    if x < 1:
        return '0'
    return ''.join(str(x % base) for x in range(x, 0, -base))

