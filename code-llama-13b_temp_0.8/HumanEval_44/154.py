

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
    if not (0 <= base <= 10):
        raise ValueError("base must be between 1 and 10")
    if not (0 <= x):
        raise ValueError("number must be positive")
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])

