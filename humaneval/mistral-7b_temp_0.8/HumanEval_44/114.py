

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

    if base < 2 or base > 10:
        raise ValueError("Base numbers are less than 10.")

    if x < 0:
        raise ValueError("Input number can not be negative.")

    remainder = x % base
    x //= base
    if x == 0:
        return str(remainder)
    return change_base(x, base) + str(remainder)

