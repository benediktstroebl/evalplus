

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
    if base <= 9:
        str_num = ''
        while x:
            x, remainder = divmod(x, base)
            str_num = str(remainder) + str_num
        return str_num
    else:
        raise ValueError("base cannot be bigger than 10")

