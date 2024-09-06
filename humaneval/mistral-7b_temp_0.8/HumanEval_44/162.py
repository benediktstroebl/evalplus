

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
        raise ValueError(f"Invalid base number. It should be less than 10.")
    if x < 0:
        raise ValueError("Negative numbers can't be changed to base")
    r = ""
    while x != 0:
        r += str(x % base)
        x //= base
    return r[::-1]

