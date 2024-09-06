

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
        raise ValueError("base must be in the range [2, 10]")
    if x < 0:
        sign = -1
    elif x == 0:
        return 0
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(int(x % base))
        x = x // base
    if sign < 0:
        digits.append(sign)
    return ''.join(str(x) for x in digits[::-1])
