

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
    base = base
    if x == 0:
        return str(0)
    total = 0
    y = [ i for i in range(base**3, 0, -1) if x & i == i]
    if len(y) == 0:
        return str(x)
    for index, value in enumerate(y):
        total += value * (base ** (len(y) -1 - index))
    return str(total)
