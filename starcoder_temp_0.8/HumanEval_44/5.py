

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
    if base > 10:
        raise ValueError("base can't be greater than 10")
    if not x:
        return '0'
    digits = string.digits
    return (change_base(x // base, base) + digits[x % base])
