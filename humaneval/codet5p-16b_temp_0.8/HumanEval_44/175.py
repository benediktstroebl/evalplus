

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

    assert base > 1, 'base number should be more than 1'
    assert x >= 0, 'number should be positive'

    if x == 0:
        return '0'

    result = []
    while x > 0:
        result.append(chr(ord('0') + x % base))
        x //= base
    return ''.join(reversed(result))

