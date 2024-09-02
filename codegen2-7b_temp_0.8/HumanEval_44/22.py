

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
    if base > 10 or base < 2:
        raise ValueError('base must be from 2 to 10')
    if base == 2:
        return bin(x)[2:]
    if base == 10:
        return str(x)
    return ''.join([str(c) for c in map(lambda i: int(i) * base, str(x))])
