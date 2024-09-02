

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
    # FIXME
    def to_base(x, b):
        digits = '0123456789ABCDEFGHIJ'
        if x < b:
            return digits[x]
        else:
            return to_base(x // b, b) + digits[x % b]
    return to_base(x, base)
