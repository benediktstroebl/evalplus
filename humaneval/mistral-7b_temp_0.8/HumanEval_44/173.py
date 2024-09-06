

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
    x_string = str(x)
    x_list = list(x_string)
    x_list.reverse()

    base_string = ''
    while x_list:
        x = int(x_list.pop())
        base_string += str(x % base)

    return base_string

