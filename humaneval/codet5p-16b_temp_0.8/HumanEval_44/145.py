

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
        return None
    if base == 10:
        return str(x)
    result = []
    while x:
        result.append(chr(48 + x % base))
        x //= base
    return ''.join(result[::-1])
