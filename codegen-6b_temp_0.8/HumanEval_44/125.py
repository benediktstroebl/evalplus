

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
    convert_int = lambda x: x >= 0 and chr(ord('0') + x) or chr(ord('a') + x)
    convert_base = lambda x: base -10 * x
    n = convert_int(x)
    result = ''
    while n > 0:
        result = convert_base(n % base) + result
        n //= base
    return result

