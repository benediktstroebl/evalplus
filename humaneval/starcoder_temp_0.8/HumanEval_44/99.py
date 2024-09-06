

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
    digits = string.digits[:10]
    if x < 0:
        return "-" + change_base(-x, base)
    if base < 2 or base > 10:
        raise ValueError("Base needs to be between 2-10")

    result = ""
    while x >= base:
        result = digits[x % base] + result
        x = x // base
    result = digits[x % base] + result

    return result
