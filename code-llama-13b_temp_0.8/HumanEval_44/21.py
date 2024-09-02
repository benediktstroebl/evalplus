

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
    result = ""
    if not x == 0:
        if x < 0:
            x *= -1
            result += "-"
        remainder = x % base
        result = str(remainder) + result
        change_base(x // base, base)
    return result
