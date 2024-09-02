

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
    if base <= 10:
        return str(x)

    new_base = []

    while x:
        new_base.append(chr(ord('0') + x % base))
        x //= base

    new_base.reverse()
    return "".join(new_base)

