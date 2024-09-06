

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
    digits = [str(digit) for digit in x]
    result = ''
    while x > 0:
        result = str(digits.pop(0)) + result
        x //= base
    return result
