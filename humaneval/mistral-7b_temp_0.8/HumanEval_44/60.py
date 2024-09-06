

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

    # 下面一句写法
    # if base < 2 or base > 10:
    #     return "Wrong base number"

    # 上面一句写法
    if base not in range(2, 11):
        return "Wrong base number"

    x = int(x)
    result = ""
    while x != 0:
        remainder = x % base
        x = x // base
        result = str(remainder) + result
    return result

