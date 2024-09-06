

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
    digits = "0123456789ABCDEF"
    signs = "+-"
    res = ""
    if abs(x) == 0:
        return "0"
    while abs(x) != 0:
        res += digits[abs(x) % base]
        x //= base
    if x < 0:
        res += signs[-abs(x)]
    return res[::-1]
