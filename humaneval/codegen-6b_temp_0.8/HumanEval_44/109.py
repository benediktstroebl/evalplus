

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
    change_allowed = [str(i) for i in range(10)]
    if x < 10:
        return str(x)
    else:
        if x < 100:
            return change_base(x // 10, base) + change_allowed[x % 10]
        else:
            return change_base(x // 100, base) + change_allowed[x % 10] + change_allowed[x % 100 // 10]

