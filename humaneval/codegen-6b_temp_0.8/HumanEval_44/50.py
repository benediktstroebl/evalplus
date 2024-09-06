

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
        raise ValueError

    digits = []
    while x:
        digits.append(x % base)
        x //= base
    if digits[-1] == 0:
        digits = digits[:-1]

    return "".join([str(x) for x in digits[::-1]])
