

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
    # check the base numbers are less than 10.
    if base < 10:
        return str(x)

    else:
        return change_base(x, base - 10) + str(x % base)
