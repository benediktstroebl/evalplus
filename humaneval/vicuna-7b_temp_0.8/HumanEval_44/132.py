

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
    if base not in [2, 3, 4, 5, 6, 7, 8, 9]:
        return x
    digits = {}
    while x > 0:
        digit = x % base
        x //= base
        digits[digit] = digits.get(digit, 0) + 1
    result = ''
    while x != 0:
        digit = x % base
        result = digit + result[result.rfind(str(digit)) + 1:] * (10 ** (len(digits) - 1 - int(digits[digit])))
        x //= base
    return result
