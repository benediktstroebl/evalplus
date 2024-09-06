

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
    base = abs(base)
    digits = []
    while x != 0:
        digits.append(x % base)
        x = x // base
    return ''.join(str(digit) for digit in digits[::-1])

