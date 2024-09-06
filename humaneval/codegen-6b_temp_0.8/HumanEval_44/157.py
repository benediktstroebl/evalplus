

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
    # convert number to a string
    y = str(x)
    # base numbers less than 10
    if base < 10:
        # if base is less than 10, return the number in new base
        return y[::-1].zfill(base)[::-1]
    else:
        # if base is larger than 10, recurse
        return change_base(y, base - 10)

