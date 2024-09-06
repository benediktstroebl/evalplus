

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
    base_len = len(str(base))
    x_copy = x
    result = ''
    while x_copy > 0:
        result = str(x_copy % base) + result
        x_copy //= base
    length = 0
    while x > 0:
        x //= base
        length += 1
    for _ in range(base_len - length):
        result = '0' + result
    return result
