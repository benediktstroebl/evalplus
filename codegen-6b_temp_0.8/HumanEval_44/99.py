

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
    base_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x < base:
        return base_string[x]
    return change_base(x//base, base) + base_string[x % base]
