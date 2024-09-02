

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
    rem = []
    while x > 0:
        rem.append(x % base)
        x = x // base
    rem = [str(x) for x in rem[::-1]]
    return ''.join(rem)

