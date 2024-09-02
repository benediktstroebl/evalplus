

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
    if not isinstance(x, int):
        raise TypeError("input x is not integer")
    if not isinstance(base, int):
        raise TypeError("input base is not integer")
    if base > 10 or base < 2:
        raise ValueError("input base is not in between 2 and 10")
    res = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while x > 0:
        remainder = x % base
        res = digits[remainder] + res
        x //= base
    return res

