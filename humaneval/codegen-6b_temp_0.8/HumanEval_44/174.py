

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
        x *= -1
        s = ''
        while x > 0:
            x, d = divmod(x, base)
            s = chr(ord('0') + d) + s
        return s
    digits = set(str(x))
    if len(digits) == 1:
        digits.add('0')
    s=''
    while x > 0:
        x, d = divmod(x, base)
        s = chr(ord('0') + d) + s
    return s

