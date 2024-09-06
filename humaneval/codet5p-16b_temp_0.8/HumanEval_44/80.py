

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

    if base < 2:
        raise ValueError("Base number should be greater than 2")
    if base > 36:
        raise ValueError("Base number should be less than 36")
    while x:
        yield str(x % base)
        x //= base
