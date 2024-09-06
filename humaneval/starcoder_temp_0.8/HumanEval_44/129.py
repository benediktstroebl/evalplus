

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

    def to_string(n, base):
        digits = '0123456789ABCDEF'
        if n < base:
            return digits[n]
        return to_string(n // base, base) + digits[n % base]

    return to_string(x, base)

