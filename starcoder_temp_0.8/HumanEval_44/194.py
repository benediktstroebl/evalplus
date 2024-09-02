

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
    assert 2 <= base <= 10, "base is out of range."
    assert x >= 0, "x must be >= 0."
    if x == 0:
        return '0'
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))

