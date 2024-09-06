

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
    temp_str = ''
    temp_num = x
    temp_base = base
    while temp_num > 0:
        temp_str = str(temp_num % temp_base) + temp_str
        temp_num = temp_num // temp_base
    return temp_str

