

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
    str_x = f"{x}"
    lst = list(str_x)
    lst = [int(x) for x in lst]
    str_lst = list(map(lambda x: f"{x:03b}", lst))
    return "".join(str_lst)
