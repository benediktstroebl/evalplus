

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
    string_representation = ''
    while x > 0:
        remainder = x % base
        string_representation = str(remainder) + string_representation
        x = int(x/base)
    return string_representation
