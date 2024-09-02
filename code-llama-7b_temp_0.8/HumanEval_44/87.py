

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
    assert 2 <= base <= 10
    digits = '0123456789ABCDEF'
    if x == 0:
        return '0'
    pos = 1
    result = ''
    while pos <= x:
        result = digits[x % base] + result
        pos *= base
        x //= base
    return result

