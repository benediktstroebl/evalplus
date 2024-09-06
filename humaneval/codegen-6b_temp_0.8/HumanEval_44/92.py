

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
        return '-' + change_base(-x, base)
    elif x == 0:
        return '0'
    digits = []
    while x:
        x, i = divmod(x, base)
        digits.append(int(i))
    return ''.join(str(d) for d in digits[::-1])

