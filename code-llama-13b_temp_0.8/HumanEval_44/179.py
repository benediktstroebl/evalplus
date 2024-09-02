

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
    # your code
    if x == 0:
        return '0'
    div = x
    mod = 0
    l = []
    while div > 0:
        mod = div % base
        l.append(mod)
        div = div // base
    s = ''
    for i in reversed(l):
        s = s + str(i)
    return s

