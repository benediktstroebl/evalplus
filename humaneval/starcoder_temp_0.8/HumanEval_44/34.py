

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
    # Convert input int to list of digits
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    # Convert list of digits to string of equivalent base
    return ''.join(str(i) for i in reversed(digits))
