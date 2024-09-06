

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
    if not 0 <= base <= 9:
        raise ValueError("Invalid base")
    digits = [0] * 10
    while x > 0:
        digits[x % base] = digits[x % base] + (x // base)
        x //= base
    return ''.join(map(str, digits))