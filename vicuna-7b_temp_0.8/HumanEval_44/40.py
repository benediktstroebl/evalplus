

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
    base_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    result = ''
    while x > 0:
        result = x % base_digits[i] + result
        x = x // base_digits[i]
        i += 1
    if x != 0:
        result = '0' + result
    return result
