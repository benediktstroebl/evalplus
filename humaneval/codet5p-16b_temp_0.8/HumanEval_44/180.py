

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

    assert 2 <= base <= 36, 'base number not in the range 2 to 36'
    if base > 10:
        base_num = change_base(x, base // 2)
        return base_num + base_num[-1]
    return str(x)

