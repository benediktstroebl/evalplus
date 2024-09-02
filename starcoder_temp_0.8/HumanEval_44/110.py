

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
    if not 1 <= x < 10:
        raise ValueError("Only support 1-10")

    if x == 0:
        return "0"
    if base == 1:
        return "1"

    output = ""
    while x > 0:
        output = str(x % base) + output
        x //= base
    return output
