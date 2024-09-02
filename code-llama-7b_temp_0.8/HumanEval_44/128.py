

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

    # 取得余数并转换为字符，加入列表中
    str_list = []
    while x >= base:
        str_list.append(str(x % base))
        x = x // base

    # 加入剩下来的余数
    str_list.append(str(x))
    str_list.reverse()
    return "".join(str_list)
