

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
    if base == 1:
        return str(x)
    if x < base:
        return ""
    result = ""
    if x < base ** 2:
        result += str(x % base)
        x //= base
        if x > 0:
            result += '*'
            result += str(x)
    else:
        result = str(x)
    return result
