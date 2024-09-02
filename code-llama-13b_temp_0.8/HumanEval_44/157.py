

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
    result = ''
    if x == 0:
        return '0'
    while x > 0:
        if x % base > 9:
            result += chr(64 + x % base)
        else:
            result += str(x % base)
        x //= base
    return result[::-1]

