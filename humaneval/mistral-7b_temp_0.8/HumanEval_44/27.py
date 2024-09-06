

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

    if base < 2:
        raise ValueError("The base cannot be less than 2.")
    if x < 0:
        raise ValueError("The number x cannot be less than 0.")
    if x < base:
        return str(x)

    binary = ""
    while x >= base:
        if x % base < 10:
            binary = str(x % base) + binary
        else:
            binary = chr(x % base + 55) + binary
        x //= base

    return binary

