

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

    change_num = change_base(x, base)
    num = ""
    for i in range(len(change_num)):
        if int(change_num[i]) >= base:
            num += str(int(change_num[i]) % base)
        else:
            num += str(int(change_num[i]))
    return num

