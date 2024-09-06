

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

    convert_base_10 = change_base_10(x, base)
    convert_base_10 = int(convert_base_10)
    convert_base_10 = list(str(convert_base_10))
    convert_base_10.reverse()
    convert_base_10 = ''.join(convert_base_10)
    return convert_base_10

