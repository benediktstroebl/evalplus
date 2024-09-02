

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
    if base > 10:
        return change_base(x, base % 10)
    if x == 0:
        return '0'
    elif x == 1:
        return str(x)
    elif x == 2:
        return change_base(x // 2, base) + str(x % 2)
    elif x == 3:
        return change_base(x // 3, base) + str(x % 3)
    elif x == 4:
        return change_base(x // 4, base) + str(x % 4)
    elif x == 5:
        return change_base(x // 5, base) + str(x % 5)
    elif x == 6:
        return change_base(x // 6, base) + str(x % 6)
    elif x == 7:
        return change_base(x // 7, base) + str(x % 7)
    elif x == 8:
        return change_base(x // 8, base) + str(x % 8)
    elif x == 9:
        return change_base(x // 9, base) + str(x % 9)
    else:
        return change_base(x // 10, base) + str(x % 10)
