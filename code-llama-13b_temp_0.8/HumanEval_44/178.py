

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
        raise ValueError('base must be >= 2.')

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base_10 = 0
    while x > 0:
        base_10 += x % base * 10
        x //= base

    if base_10 == 0:
        return '0'

    return_str = ''
    while base_10 > 0:
        return_str += digits[base_10 % 10]
        base_10 //= 10

    return return_str[::-1]

