

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

    conversion = '0123456789ABCDEF'
    remainder_stack = []
    while x!= 0:
        remainder = x % base
        x = x // base
        remainder_stack.append(remainder)
    string = ''
    while remainder_stack:
        string += conversion[remainder_stack.pop()]
    return string

