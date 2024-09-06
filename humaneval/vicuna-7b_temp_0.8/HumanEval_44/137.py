

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
    digits = str(x)
    result = ""
    while digits:
        i = digits.index(str(x // base))
        result += str(x % base)
        x = base * i
        digits = digits[:i]
    return result
