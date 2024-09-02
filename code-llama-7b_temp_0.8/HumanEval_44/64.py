

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
    if x < 0:
        raise ValueError('only non-negative integers are accepted.')
    if base <= 1 or base >= 10:
        raise ValueError('base must be less than 10.')
    res = ''
    while x:
        res += str(x % base)
        x //= base
    return res[::-1]

