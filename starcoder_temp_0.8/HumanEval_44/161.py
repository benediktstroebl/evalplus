

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
    x_list = []
    while x > 0:
        x, rem = divmod(x, base)
        x_list.append(rem)
    # Reverse the list
    x_list.reverse()
    return "".join(str(y) for y in x_list)
