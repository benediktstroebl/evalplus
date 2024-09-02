

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
    if not 2 <= base <= 10:
        raise ValueError("base not in range [2, 10]")
    if not isinstance(x, int):
        raise TypeError(f"Expected int, got {x.__class__}")
    if x < 0:
        sign = -1
    elif x == 0:
        return "0"
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    if sign < 0:
        digits.append("-")
    digits.reverse()
    return "".join(digits)
