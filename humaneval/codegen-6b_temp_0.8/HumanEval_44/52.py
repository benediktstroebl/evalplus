

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
    el = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    out = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if x == 0:
        return '0'
    if x == 1:
        return el[1]
    if x == 2:
        return el[2]
    if x == 3:
        return el[3]
    if x == 4:
        return el[4]
    if x == 5:
        return el[5]
    if x == 6:
        return el[6]
    if x == 7:
        return el[7]
    if x == 8:
        return el[8]
    if x == 9:
        return el[9]
    b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = ''
    while x > 0:
        r = x % base
        s = b[r] + s
        x //= base
    return s
