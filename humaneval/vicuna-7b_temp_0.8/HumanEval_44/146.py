

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
    result = ''
    while digits:
        rem, x = divmod(x, digits[0])
        x = rem // digits[0]
        result = digits[0] + result
        digits = rem % digits[0]
    return result
