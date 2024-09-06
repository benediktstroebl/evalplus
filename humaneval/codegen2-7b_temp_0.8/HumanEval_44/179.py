

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
    str_number = str(x)
    str_base = str(base)

    if base == 10:
        return str_number

    if str_base == '10':
        return int(str_number)

    if str_number[0] == '-':
        str_number = str_number[1:]

    return int(str_number, str_base)
