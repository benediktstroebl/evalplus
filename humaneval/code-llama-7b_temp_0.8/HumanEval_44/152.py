

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
    if x < 0:
        raise ValueError("input x must be positive")
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")

    res = ""
    while x >= base:
        res += str(x % base)
        x //= base

    if x > 0:
        res += str(x)

    return res[::-1]
