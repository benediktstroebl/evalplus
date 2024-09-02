

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
    assert x >= 0 and base < 10 and base > 1, 'invalid base'
    x_list = []
    while x >= base:
        x_list.append(str(x % base))
        x = x // base
    x_list.append(str(x))
    return ''.join(x_list[::-1])

