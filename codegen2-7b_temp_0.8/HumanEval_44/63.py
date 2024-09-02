

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
    new_base = ""
    if base < 10:
        raise ValueError("base must be less than 10")

    if x < 0:
        new_base = "-"
        x = abs(x)

    while x:
        x, remainder = divmod(x, base)
        new_base = str(remainder) + new_base

    return new_base
