

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
    if base == 10:
        return str(x)
    digits = "0123456789ABCDEF"
    temp = x
    result = ""
    while temp > 0:
        result += digits[temp % base]
        temp //= base
    return result[::-1]

