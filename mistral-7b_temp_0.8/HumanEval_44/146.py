

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
    s = str(x)
    l = len(s)
    for i in range(l - 1, -1, -1):
        s[i] = chr(ord('0') + int(s[i]) // base)
        if s[i] != '0':
            break
    return s

