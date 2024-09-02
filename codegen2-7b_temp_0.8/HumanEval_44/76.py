

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
    if base < 10:
        raise ValueError('Cannot convert non-base number to base %d.' % base)
    num_as_string = str(x)
    new_number = int(num_as_string, base)
    return str(new_number)

