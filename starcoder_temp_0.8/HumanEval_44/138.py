

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
    assert 0 <= x < 10**10, "x must be between 0 and 10**10"
    assert 0 < base <= 10, "base must be between 0 and 10"
    if base == 10:
        return str(x)
    digits = ''
    while x > 0:
        x, r = divmod(x, base)
        digits += str(r)
    return digits[::-1]
