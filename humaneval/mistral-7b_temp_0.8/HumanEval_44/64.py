

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

    base = int(base)
    if base < 2 or base > 10:
        raise ValueError('invalid base')
    num = []
    while x > 0:
        num.append(int(x % base))
        x = x // base

    num.reverse()
    return ''.join(str(num))

