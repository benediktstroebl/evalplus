

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
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)

    base_representation = ''
    while x > 0:
        remainder = x % base
        x //= base
        if remainder <= 9:
            remainder = str(remainder)
        else:
            remainder = chr(ord('a') + remainder - 10)
        base_representation = remainder + base_representation
    return base_representation

