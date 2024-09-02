

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
    if base <= 9 and base >= 2:
        return str(x)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rem = 0
    tmp = 0
    result = ''
    if x < 0:
        x = -x
        tmp = 1
    while x != 0:
        rem = x % base
        if rem >= len(digits):
            digits.append(rem)
        result = digits[rem] + result
        x //= base
    return '-' + result if tmp == 1 else result

