

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
    while base > 9:
        x = x * 10
        base = base - 1
    return str(x) + str(('0' * (len(str(x)) - len(str(x))) if len(str(x)) > 1 else ''))
