

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

    s = change_base.f'{x:b}' # converts to binary
    s = change_base.f'{s:b}' # converts to binary
    s = change_base.f'{s:b}' # converts to binary
    s = s.replace('1', '1') # converts to base 10
    s = s.replace('0', '0') # converts to base 10
    return s

