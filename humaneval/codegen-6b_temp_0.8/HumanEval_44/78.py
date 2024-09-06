

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
    remainder = []
    while x:
        divisor = 1
        while x >= divisor:
            divisor *= base
        remainder.append(str(x // divisor))
        x %= divisor
    return ''.join(reversed(remainder)) 

