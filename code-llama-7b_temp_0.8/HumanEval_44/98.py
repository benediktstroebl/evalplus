

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
    if x < 0:
        raise ValueError('Input x must be a positive integer.')
    if base < 2:
        raise ValueError('Base must be greater than or equal to 2.')
    if base >= 10:
        raise ValueError('Base must be less than 10.')
    quotient = x
    remainder = 0
    digits = []
    while quotient != 0:
        remainder = quotient % base
        digits.append(remainder)
        quotient = quotient // base
    return ''.join(str(i) for i in digits[::-1])

