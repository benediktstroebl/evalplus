

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

    if x == 0:
        return "0"

    x_list = []

    while x:
        x_list.append(x % base)
        x = x // base

    return "".join(map(str, x_list[::-1]))

