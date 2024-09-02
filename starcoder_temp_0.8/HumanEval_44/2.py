

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
    base_num = "0123456789ABCDEF"
    if x == 0:
        return "0"
    base_list = []
    while x:
        base_list.append(x % base)
        x //= base
    base_list.reverse()
    return "".join(map(lambda x: base_num[x], base_list))
