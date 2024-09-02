

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
    if x >= base:
        raise ValueError("number should be less than base")
    digits = ""
    while x:
        digits = str(base) + digits
        x, remainder = divmod(x, base)
    return digits[::-1
