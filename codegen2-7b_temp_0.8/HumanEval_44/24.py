

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
    result = ''
    while x > 0:
        remainder = x % base
        x = x // base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder + ord('A') - 10) + result
    return result
