

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
        raise ValueError("Base should be less than 2")
    if base > 36:
        raise ValueError("Base should be less than 36")
    if x < 0:
        return '-' + change_base(-x, base)
    if x == 0:
        return '0'
    n = ''
    while x > 0:
        n = str(x % base) + n
        x = x // base
    return n

