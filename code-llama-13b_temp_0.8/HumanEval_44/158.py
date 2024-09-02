

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
    assert 1 <= base <= 9

    if x == 0:
        return '0'
    if x < 0:
        sign = '-'
        x = -x
    else:
        sign = ''

    digits = []
    while x > 0:
        x, y = divmod(x, base)
        digits.append(str(y))

    return sign + ''.join(reversed(digits))

