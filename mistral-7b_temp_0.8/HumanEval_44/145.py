

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
    if base < 2 or base > 10:
        raise ValueError("base is outside the range of 2-10")
    if x < 0:
        return "invalid number"
    if x == 0:
        return str(x)
    new_string = ""
    while x != 0:
        rem = x % base
        new_string = str(rem) + new_string
        x = x // base
    return new_string

