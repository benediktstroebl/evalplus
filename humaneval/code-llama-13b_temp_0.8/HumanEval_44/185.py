

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
    string_digits = []
    while x > 0:
        digit = x % base
        string_digits.insert(0, str(digit))
        x = x // base
    return ''.join(string_digits)

