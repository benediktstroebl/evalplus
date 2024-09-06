

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
    if base < 10:
        raise ValueError("base should be less than 10")
    table = "0123456789"
    digits = ""
    while x:
        remainder = x % base
        digits = table[remainder] + digits
        x = x // base
    return
