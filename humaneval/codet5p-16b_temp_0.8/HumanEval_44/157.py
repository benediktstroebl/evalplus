

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

    if x == 0:
        return '0'
    if base < 2:
        raise ValueError('Base number must be greater than 1')
    digits = []
    while x > 0:
        x, d = divmod(x, base)
        digits.append(d)
    return change_base(base, base) + ''.join(map(str, digits[::-1]))

