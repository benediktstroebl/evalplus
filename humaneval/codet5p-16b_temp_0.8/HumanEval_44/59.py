

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
        raise ValueError('Invalid base number. It must be less than 10.')
    if x == 0:
        return str(x)
    new_x = []
    while x > 0:
        new_x.append(x % base)
        x //= base
    new_x.reverse()
    return change_base(sum(list(map(lambda x: x*(base**i), new_x))), 10)
