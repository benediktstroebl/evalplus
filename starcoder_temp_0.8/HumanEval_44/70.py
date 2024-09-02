

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

    # Handle invalid inputs
    assert x >= 0 and base >= 2
    if base < 10:
        assert x < 10 * base

    # Convert digits of x into output number
    x_str = ""
    while x > 0:
        x_str = str(x % base) + x_str
        x //= base
    return x_str
