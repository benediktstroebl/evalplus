

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
    # TODO
    digits = '0123456789abcdef'
    digits = digits[:base]
    if x < 0:
        raise ValueError("Negative numbers are not allowed")
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16")
    if x == 0:
        return '0'
    x = str(x)
    return ''.join(digits[int(a)] for a in x[::-1])

