

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
    l = []
    c = x
    while True:
        quotient, remainder = divmod(c, base)
        l.append(str(remainder))
        if quotient == 0:
            break
        c = quotient
    return ''.join(l)

