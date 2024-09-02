

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
    return_val = ""
    tmp_x = x
    count = 0
    while x > 0:
        if base == 2:
            return_val = str(x % 2) + return_val
        elif base == 3:
            return_val = str(x % 3) + return_val
        elif base == 4:
            return_val = str(x % 4) + return_val
        else:
            return_val = str(x % 10) + return_val
        x = tmp_x // base
        count += 1
    return return_val

