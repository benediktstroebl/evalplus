

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
    d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    if x == 0:
        return '0'
    digits = []
    while x > 0:
        digits.append(x % base)
        x = x // base
    res = ''
    for i in reversed(digits):
        res += str(i)
    if res[-1] == '0':
        return res[:-1]
    return res
