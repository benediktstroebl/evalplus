

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
    if not 0 < base < 10:
        raise ValueError("base should be between 0 and 10.")

    result = ""

    while x:
        remainder = x % base
        x = x // base
        result = str(remainder) + result

    return result

