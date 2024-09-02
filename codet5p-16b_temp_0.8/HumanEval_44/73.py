

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

    x_str = str(x)
    base_num = []
    for i in range(len(x_str)):
        base_num.append(x_str[i])

    res = 0
    for i in range(len(base_num)):
        res += int(base_num[i]) * base ** (len(base_num) - 1 - i)
    return str(res)
