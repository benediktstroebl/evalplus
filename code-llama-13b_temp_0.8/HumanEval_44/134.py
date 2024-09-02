

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
    # convert integer x to list of digits
    digits = []
    y = x
    while y > 0:
        digits.append(y % base)
        y = y // base
    # reverse list of digits
    digits = digits[::-1]
    # convert each digit to character and return
    return ''.join(str(digit) for digit in digits)

