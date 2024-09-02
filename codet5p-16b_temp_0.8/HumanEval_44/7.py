

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

    if base < 2:
        raise ValueError('Bases less than 2 not supported.')
    if base > 10:
        raise ValueError('Bases greater than 10 not supported.')
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        remainder = x % base
        x = x // base
        result = str(remainder) + result
    return result

