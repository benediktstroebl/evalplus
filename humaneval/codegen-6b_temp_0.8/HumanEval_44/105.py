

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
    x = abs(x)
    digits = []
    if x == 0:
        return "0"
    while x > 0:
        digits.append(int(x % base))
        x //= base
    digits = reversed(digits)
    return "".join(str(d) for d in digits)
