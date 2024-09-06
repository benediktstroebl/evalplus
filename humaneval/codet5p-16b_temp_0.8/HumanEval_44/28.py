

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
        return change_base(-x, base)
    if base < 2 or base > 16:
        return ''
    result = ''
    while x > 0:
        remainder = x % base
        if remainder > 9:
            remainder = change_base(remainder, 10)
        result += str(remainder)
        x //= base
    return result[::-1]
