

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
    assert base < 10, 'base must be less than 10'
    num_str = str(x)
    # 不断除10，拿到余数
    i = 0
    while x != 0:
        x = x // base
        num_str = str(x % base) + num_str
        i += 1
    return num_str
