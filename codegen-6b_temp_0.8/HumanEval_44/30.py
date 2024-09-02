

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
    y = list()
    if x < 0:
        y.append('-')
        x = abs(x)
    if x == 0:
        return '0'
    while x > 0:
        a = x % base
        y.append(str(a))
        x = x // base
    while y[-1] == '0':
        y.pop()
        if y == []:
            y.append('0')
    y.reverse()
    y = ''.join(y)
    return y
