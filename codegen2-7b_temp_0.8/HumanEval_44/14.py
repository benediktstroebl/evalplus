

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
    s = ""
    if base < 2 or base > 16:
        print('base must be between 2 and 16')
        return None
    while x > 0:
        remainder = x % base
        s = chr(remainder + 65) + s
        x //= base
    return
