

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
    convert_to_decimal = x/base
    convert_to_decimal_list = list(str(convert_to_decimal))
    new_list = []
    for value in convert_to_decimal_list:
        new_list.insert(0, value)
    new_list = ''.join(new_list)
    return new_list

