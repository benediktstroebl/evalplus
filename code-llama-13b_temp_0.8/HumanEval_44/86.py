

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

    assert x >= 0, "x must be a positive number"
    assert base > 0 and base <= 10, "base must be between 1 and 10"
    s = ""
    while x > 0:
        s = str(x % base) + s
        x //= base
    return s
