

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

    assert 2 <= base <= 10, 'Base should be in range 2-10'
    if base == 10:
        return str(x)
    else:
        result = ''
        while x > 0:
            result = str(x % base) + result
            x //= base
        return result

