

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
    if not 0 <= x < base**2:
        raise ValueError("Input number out of range")
    if x == 0:
        return "0"
    digits = []
    while x:
        digits.append(x % base)
        x //= base
    return "".join(map(str, digits[::-1]))



