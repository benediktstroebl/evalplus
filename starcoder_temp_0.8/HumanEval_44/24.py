

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
    assert x >= 0, "x must be a non-negative integer"
    assert base >= 2, "base must be at least 2"

    base_digits = "0123456789ABCDEF"
    digits = []

    while x:
        x, rem = divmod(x, base)
        digits.append(base_digits[rem])

    digits.reverse()
    return "".join(digits)
