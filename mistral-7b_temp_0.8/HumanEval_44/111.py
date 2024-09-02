

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
    assert (base >= 2 and base <= 10), "base number should be between 2 and 10"
    x_list = []
    while x > 0:
        x_list.append(str(x % base))
        x = x // base
    return ''.join(reversed(x_list))

