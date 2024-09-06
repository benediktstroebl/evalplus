

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
    convert_digits = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    result = ""
    while x > 0:
        if x % base > 9:
            result += str(convert_digits[x % base])
        else:
            result += str(x % base)
        x //= base
    result = result[::-1]
    return result
