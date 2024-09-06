

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
    i = 0
    num = ""
    while x != 0:
        r = x % base
        if r < 10:
            r = str(r)
        else:
            r = chr(r + 87)
        num = r + num
        x = x // base
        i += 1
    return num

