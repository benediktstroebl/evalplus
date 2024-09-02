

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
    assert x <= 9 and base <= 10, 'Invalid base'
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result

